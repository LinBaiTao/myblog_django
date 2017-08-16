#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author:LinBaiTao

from django.conf.urls import url

from . import views

app_name = 'blog'
# 两个括号括起来的地方是两个命名组参数，Django 会从用户访问的 URL 中自动提取这两个参数的值，然后传递给其对应的视图函数

# # *************************视图函数式写法*********************************
# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
#     url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
#     url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
# ]


# ***************************基于视图类写法*************************
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
]
