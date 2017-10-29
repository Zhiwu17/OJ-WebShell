from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.views.generic import ListView
from execise.models import Solution, Problem, Compileinfo


class UserSolutionList(ListView):
    
#    solution = Solution.objects.filter(user_id=user_id)
#    return HttpResponse('user_id'+str(solution.count()))
#    return render_to_response('userSolutList.html', {object_list:solution}, RequestContext(req))
    
#    def get(self, req, user_id=''):
#        return HttpResponse('user_id '+user_id)
#        return Solution.objects.filter(user_id=user_id)

    def get_queryset(req, user_id=''):
        solution = Solution.objects.filter(user_id=user_id)
        return {'user_id':user_id}

def userSolutionList(req, user_id=''):

    switch = {
        2:'编译中',
        3:'运行并编译',
        4:'正确',
        5:'格式错误',
        6:'答案错误',
        7:'时间超限',
        8:'内存超限',
        9:'输出超限',
        10:'运行错误',
        11:'编译错误',
        }
    
    solution = Solution.objects.filter(user_id=user_id)
    for i in solution:
        title = Problem.objects.get(problem_id=i.problem_id).title
#        result = Compileinfo.objects.get(solution_id=i.solution_id).result
        i.title = title
        i.result = switch[i.result]
#    return solution
    return render_to_response('userSolutList.html', {'object_list':solution}, RequestContext(req))
