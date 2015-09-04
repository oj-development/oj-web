from django import forms
from .proglang import proglang
from .result_name import *
allresult=(("","All"),)

class RegisterPage(forms.Form):
    user_id = forms.CharField(label='User ID', max_length=100)
    password = forms.CharField(label='Password', max_length=100,widget=forms.PasswordInput())
    rptpassword = forms.CharField(label='Repeat Password', max_length=100,widget=forms.PasswordInput())
    nick_name = forms.CharField(label='Nick Name', max_length=100,required=False)
    
class SubmitPage(forms.Form):
    language = forms.ChoiceField(label='Language', choices=proglang)
    source = forms.CharField(label='Source code',widget=forms.Textarea())
    
class StatusSearch(forms.Form):
    problem_id = forms.IntegerField(label='Problem ID',required=False)
    user_id = forms.CharField(label='User ID',required=False)
    language = forms.ChoiceField(label='Language', choices=allresult+proglang,required=False)
    result = forms.ChoiceField(label='Result', choices=allresult+result_tuple,required=False)
    