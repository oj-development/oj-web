"""oj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
import os

urlpatterns = [
    url(r'^$', 'oj_core.views.index', name='index'),
    url(r'^problem/(?P<problem_id>[^/]+)/$', 'oj_core.views.show_problem', name='problem'),
    url(r'^submit/(?P<problem_id>[^/]+)/$', 'oj_core.views.submit', name='submit'),
    url(r'^problemset/', 'oj_core.views.problem_set', name='problemset'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'), 
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}, name='logout'), 
    url(r'^register/$', 'oj_core.views.registerpage', name='registerpage'),
    url(r'^userinfo/(?P<user_id>[^/]+)/$', 'oj_core.views.userinfo', name='userinfo'),
    url(r'^status/', 'oj_core.views.status', name='status'),
    url(r'^ranklist/', 'oj_core.views.ranklist', name='ranklist'),
]+static('/static/', document_root=os.path.join(settings.BASE_DIR,'static'))
