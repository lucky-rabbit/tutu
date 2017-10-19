#coding:utf-8

from django.conf.urls import url
from . import views

#指定命名空间,告诉Django这个模块属于blog应用
app_name = 'blog'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	#(?P<pk>[0-9]+)匹配数字并保存为{pk:99}的字典
	url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
	url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
	url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]