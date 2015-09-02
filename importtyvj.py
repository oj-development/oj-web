from oj.wsgi import *
from oj_core.models import Problem, Data
import os, hashlib, sys, tyvj2json
def getfile(filename):
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            return f.read()
    else:
        return ""
def main(problem_name):
    os.chdir(problem_name)
    tyvj2json.main()
    problem_content={
        'name':problem_name,
        'background':getfile('Background.txt'),
        'description':getfile('Description.txt'),
        'input':getfile('InputFormat.txt'),
        'output':getfile('OutputFormat.txt'),
        'sample_input':getfile('SampleInput.txt'),
        'sample_output':getfile('SampleOutput.txt'),
        'time_limitation':getfile('TimeLimitation.txt'),
        'hint':getfile('Hint.txt'),
        'source':getfile('Source.txt')
    }
    p=Problem.objects.get_or_create(**problem_content)
    if p[1]:
        p=p[0]
        data=getfile('export.json')
        md5 = hashlib.md5()
        md5.update(data.encode('utf-8'))
        data_hash=md5.hexdigest()
        Data.objects.create(problem=p,data_hash=data_hash)
        os.rename('export.json', os.path.join('..','data',data_hash+'.json'))
    else:
        print("Duplicate: "+problem_name)
    os.chdir("..")
if __name__ == '__main__':
    if len(sys.argv)>=2:
        for i in sys.argv[1:]:
            main(i)
    else:
        main(input())
    print("Done!")