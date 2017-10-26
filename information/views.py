from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.views.generic import ListView
from execise.models import Solution


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
    
    solution = Solution.objects.filter(user_id=user_id)
#    return solution
    return render_to_response('userSolutList.html', {'object_list':solution}, RequestContext(req))
