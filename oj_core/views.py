from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import RegisterPage, SubmitPage
from datetime import datetime, timedelta, timezone
from django.conf import settings
import json, os, socket, uuid
from .result_name import *
# Create your views here.
def_limit=100
timestamp=0
def index(request):
    return render(request, 'base.html', {})
def show_problem(request, problem_id):
    problem = Problem.objects.get(pk=problem_id)
    return render(request, 'problem.html', {'problem_id':problem_id,'problem':problem})
def problemstatus(request, problem_id):
    problem = Problem.objects.get(pk=problem_id)
    return render(request, 'problemstatus.html', {'id':problem_id,'submit':problem.submit,'ac':problem.ac,'solved':problem.solved_by.get_queryset().count(),'tried':problem.tried_by.get_queryset().count()})
def problem_set(request):
    offset = int(request.GET.get('offset','0'))
    limit = int(request.GET.get('limit',def_limit))
    all_problemset = Problem.objects.all()
    problemset = all_problemset[offset:offset+limit]
    pages=[(n,def_limit*n-def_limit) for n in range(1,(all_problemset.count()-1)//def_limit+2)]
    return render(request, 'problemset.html', {'problemset':problemset,'pages':pages,'curpage':offset//limit+1 if ((limit==def_limit) and (offset%limit==0)) else 0})
def registerpage(request):
    error=''
    if request.method == 'POST':
        form = RegisterPage(request.POST) 
        if form.is_valid():
            if form.cleaned_data['password']==form.cleaned_data['rptpassword']:
                user = User()
                user.username = form.cleaned_data['user_id']
                user.set_password(form.cleaned_data['password'])
                user.first_name=form.cleaned_data['nick_name']
                try:
                    user.save()
                except Exception as e:
                    error='User Existed!'
            else:
                error='Password Not Same!'
        else:
            error='Invalid Data!'
        if error=='':
            return render(request, 'base.html', {})
    else:
        form = RegisterPage()
    return render(request, 'registerpage.html', {'form': form, 'error': error})
def submit(request, problem_id):
    if request.method == 'POST':
        form = SubmitPage(request.POST) 
        if form.is_valid():
            data=Problem.objects.get(pk=problem_id).data_set.get_queryset()[0].data_hash
            data_send=json.dumps([1,[{"input":'',"output":'',"judgemode":7},[form.cleaned_data['language'],form.cleaned_data['source']],data]])
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('127.0.0.1', 28522))
            s.send(data_send.encode('utf-8'))
            judge_result=json.loads(s.recv(1048576).decode('utf-8'))
            if judge_result[0]==1:
                with open(os.path.join(settings.BASE_DIR,'data',data+'.json'), 'r') as f:
                    realdata=f.read()
                s.send(realdata.encode('utf-8'))
                judge_result=json.loads(s.recv(1048576).decode('utf-8'))
                while judge_result[0]==4:
                    if judge_result[1]==10:
                        form = "error!" 
                        return render(request, 'submitpage.html', {'form': form})
                    s.send(b'')
                    judge_result=json.loads(s.recv(1048576).decode('utf-8'))
            record_hash=judge_result[1]
            s.close()
            new_result=Status()
            new_result.runid=uuid.UUID(record_hash)
            new_result.language=form.cleaned_data['language']
            new_result.code=form.cleaned_data['source']
            new_result.code_length=len(form.cleaned_data['source'])
            new_result.problem=Problem.objects.get(pk=problem_id)
            if request.user.is_authenticated():
                new_result.user=UserStatus.objects.get_or_create(pk=request.user.id)[0]
            new_result.save()
            form = str(judge_result)
    else:
        form = SubmitPage()
    return render(request, 'submitpage.html', {'form': form})
def status(request):
    global timestamp
    if datetime.now().timestamp()-timestamp>10:
        for i in Status.objects.all().filter(result=jresult.R.value):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('127.0.0.1', 28522))
            s.send(json.dumps([2,str(i.runid)]).encode('utf-8'))
            judge_result=json.loads(s.recv(1048576).decode('utf-8'))
            s.close()
            if judge_result[0]==0:
                judge_result=judge_result[1]
                i.score=judge_result[1]
                final_result=jresult.AC.value
                final_time=0
                for j in judge_result[0]:
                    if j[0]!=jresult.AC.value:
                        final_result=j[0]
                    final_time=max(final_time,j[1])
                i.result=final_result
                i.time=final_time
                i.save()
                i.problem.submit=i.problem.submit+1
                if final_result==jresult.AC.value:
                    i.problem.ac=i.problem.ac+1
                i.problem.save()
                if i.user:
                    if final_result==jresult.AC.value:
                        i.user.ac=i.user.ac+1
                        if not i.user.solved_problems.get_queryset().filter(pk=i.problem.pk).exists():
                            i.user.solved_problems.add(i.problem)
                            i.user.ac_problems=i.user.ac_problems+1
                    if not i.user.tried_problems.get_queryset().filter(pk=i.problem.pk).exists():
                        i.user.tried_problems.add(i.problem)
                        i.user.submit_problems=i.user.submit_problems+1
                    i.user.submit=i.user.submit+1
                    i.user.save()
    offset = int(request.GET.get('offset','0'))
    limit = int(request.GET.get('limit',def_limit))
    status_iter = Status.objects.all()[offset:offset+limit]
    status_list=[{'id':x.pk,'userid':x.user.pk if x.user else 0,'username':x.user.get_name() if x.user else 'Anonymous','problem':x.problem.pk,'result':result_name[jresult(x.result)],'memory':x.memory,'memory':x.memory,'time':'%.0f' % (x.time*1000),'language':x.get_language_display(),'code_length':x.code_length,'submit_time':x.submit_time.astimezone(timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M:%S')} for x in status_iter]
    return render(request, 'status.html', {'status_list':status_list,'limit':limit,'prev_offset':max(offset-limit,0),'next_offset':offset+limit})
def userinfo(request, user_id):
    user=UserStatus.objects.get(pk=int(user_id))
    solved_problems=[x.pk for x in user.solved_problems.get_queryset()]
    tried_problems=list({x.pk for x in user.tried_problems.get_queryset()}-set(solved_problems))
    return render(request, 'userinfo.html', {'user_id':user_id,'username':user.get_name(),'nickname':user.get_nickname(),'ac':user.ac,'submit':user.submit,'ac_problems':user.ac_problems,'submit_problems':user.submit_problems,'solved_problems':solved_problems,'tried_problems':tried_problems})
def ranklist(request):
    offset = int(request.GET.get('offset','0'))
    limit = int(request.GET.get('limit',def_limit))
    ranklist_all=UserStatus.objects.all().order_by('-ac','submit')
    ranklist_iter=ranklist_all[offset:offset+limit]
    ranklist_list=[{'ranking':i+offset,'userid':x.pk,'username':x.get_name(),'nickname':x.get_nickname(),'ac':x.ac_problems,'submit':x.submit_problems,'ratio':'%.3f%%'%((100*x.ac/x.submit) if x.submit else 0)} for i, x in enumerate(ranklist_iter)]
    pages=[(n*def_limit-def_limit,n*def_limit-def_limit+1,n*def_limit) for n in range(1,(ranklist_all.count()-1)//def_limit+2)]
    return render(request, 'ranklist.html', {'ranklist':ranklist_list,'pages':pages})
    