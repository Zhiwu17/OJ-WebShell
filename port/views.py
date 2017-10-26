from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from port.models import Users

class UserForm(forms.Form):
    user_id = forms.CharField(label='user_id', max_length=48)
    email = forms.CharField(label='email', max_length=100)
#    ip = forms.CharField(label='ip', max_length=20)
#    accesstime = forms.DateTimeField(label='accesstime')
    password = forms.CharField(label='password', widget=forms.PasswordInput())
#    reg_time = forms.DateTimeField(label='reg_time')
    nick = forms.CharField(label='nick', max_length=100)
    school = forms.CharField(label='school', max_length=100)

class UserLoginForm(forms.Form):
    user_id = forms.CharField(label='user_id', max_length=48)
    password = forms.CharField(label='password', widget=forms.PasswordInput())

def myRegist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            user_id = uf.cleaned_data['user_id']
            email = uf.cleaned_data['email']
            ip = req.META['REMOTE_ADDR'].split(',')[0]
#            accesstime = uf.cleaned_data['accesstime']
            password = uf.cleaned_data['password']
#            reg_time = uf.cleaned_data['reg_time']
            nick = uf.cleaned_data['nick']
            school = uf.cleaned_data['school']
            Users.objects.create(user_id=user_id, email=email, ip=ip,
                password=password, nick=nick, school=school, volume=1, language=1)
            return HttpResponse('regist success!!!')
    else:
        uf = UserForm()
    return render_to_response('regist.html', {'uf':uf}, context_instance=
            RequestContext(req))

def myLogin(req):
    if req.method == 'POST':
        uf = UserLoginForm(req.POST)
        if uf.is_valid():
            user_id = uf.cleaned_data['user_id']
            password = uf.cleaned_data['password']
            user = Users.objects.filter(user_id__exact = user_id, password__exact = password)
            if user:
#                return HttpResponse('Login success!!!')
                newUser = Users.objects.get(user_id=user_id)
                response = HttpResponseRedirect('/index/')
                response.set_cookie('nick', newUser.nick, 3600)
                return response
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserLoginForm()
    return render_to_response('login.html', {'uf':uf}, context_instance=RequestContext(req))

def myLogout(req):
    response = HttpResponse('logout!!!')
    response.delete_cookie('nick')
    return response


def index(req):
    nick = req.COOKIES.get('nick', '')
    return render_to_response('index.html', locals(), RequestContext(req))


def userInfo(req, nick=''):
    return render_to_response('userInfo.html', locals(), RequestContext(req))
    return render_to_response('index.html', locals())
