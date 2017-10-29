from django.http import HttpResponse
from django.template import RequestContext
from django import forms
from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from execise.models import Problem, Solution, SourceCode, Compileinfo
from port.models import Users
import datetime


class ProblemList(ListView):
#    model = Problem
    context_object_name='problem'

    def get_queryset(self):
        problem=Problem.objects.all()
        return problem

class SolutionForm(forms.ModelForm):

    class Meta:
        model = Solution
#        fields = ('problem_id', 'user_id', 'time', 'in_date', 'language', 'ip', 'memory', 'result', 'valid', 'num', 'code_length', 'pass_rate', 'lint_error', 'judger')
        fields = ('language',)


class SourceCodeForm(forms.ModelForm):
    
    class Meta:
        model = SourceCode
        fields = ('solution_id', 'source')


def problemList(req):
#   return ProblemList.as_view(template_name='problem_list')
    return HttpResponse('llll')


def problemDetail(req, problem_id=''):
    problem = Problem.objects.get(problem_id=problem_id)
    problem_title = problem.description
    nick = req.COOKIES.get('nick')
    user = Users.objects.get(nick=nick)

    nuser_id = user.user_id
    nin_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ntime = 1
    nlanguage = 0
    nip = req.META['REMOTE_ADDR'].split(',')[0]
    nmemory = problem.memory_limit
    nvalid = 1
    nnum = -1
    npass_rate = 0.00
    nlint_error = 0
    njudger = '10.0.2.25'   

    if req.method == 'POST':
        solutionForm = SolutionForm(req.POST)
        sourceForm = SourceCodeForm(req.POST)
        nlanguage = req.POST['language']
 
        returnSoluId = Solution.objects.create(problem_id=problem_id, user_id=nuser_id, time=ntime, in_date=nin_date, language=nlanguage, ip=nip, memory=nmemory, result=0, valid=nvalid, num=nnum, code_length=200, pass_rate=npass_rate, lint_error=nlint_error, judger=njudger)

        SourceCode.objects.create(solution_id=returnSoluId.solution_id, source=req.POST['source'])
        return HttpResponse('commit successfully' + str(returnSoluId.solution_id))
    else:
        sourceForm = SourceCodeForm()
        solutionForm = SolutionForm()
##    if req.method == 'POST':
#       form = SolutionForm(req.POST)
#       sourceForm = SourceCodeForm(req.POST)
#       form.problem_id = problem_id
#      if form.is_valid():
#           solution = form.save(commit=True)
#            return HttpResponse('Commit successfully' + str(solution.solution_id))
#        else:
#                return HttpResponse('Commit badly')
#    else:
#        form = SolutionForm()
#        sourceForm = SourceCodeForm()

    return render_to_response('problem_detail.html', locals(), RequestContext(req))

def solutionDetail(req, solution_id=''):
    

    if req.method == 'GET':
        compileinfo= Compileinfo.objects.get(solution_id=solution_id)
        error = compileinfo.error
        
        return render_to_response('solutionDetail.html', locals(), RequestContext(req))
    else:
        pass
