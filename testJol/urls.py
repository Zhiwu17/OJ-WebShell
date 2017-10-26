"""testJol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from port import views as portViews
from execise import views as execiseViews
from information import views as informationViews
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', portViews.myLogin, name='myLogin'),
    url(r'^regist/', portViews.myRegist, name='myRegist'),
    url(r'^logout/', portViews.myLogout, name='myLogout'),
    url(r'^index/', portViews.index, name='index'),
    url(r'^execise/list/$', execiseViews.ProblemList.as_view(template_name='problem_list.html')),
    url(r'^execise/problem/(?P<problem_id>\d+)$', execiseViews.problemDetail, name='problemDetail'), 
    url(r'^execise/solution/(?P<solution_id>\d+)$', execiseViews.solutionDetail, name='solutionDetail'),
    url(r'^profile/(?P<user_id>.+)$', informationViews.userSolutionList, name='userProfile'),
    url(r'^userInfo/(?P<nick>.+)$', portViews.userInfo, name='userInfo'),
]
