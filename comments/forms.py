#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author:LinBaiTao


from django import forms
from .models import Comment


# Django 的表单类必须继承自 forms.Form 类或者 forms.ModelForm 类。如果表单对应有一个数据库模型（例如这里的评论表单对应着评论模型），那么使用 ModelForm 类会简单很多
# 之后我们在表单的内部类 Meta 里指定一些和表单相关的东西。model = Comment 表明这个表单对应的数据库模型是 Comment 类。fields = ['name', 'email', 'url', 'text']
# 指定了表单需要显示的字段
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']