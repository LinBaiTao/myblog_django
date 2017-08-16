#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author:LinBaiTao

from django import template
from ..models import Post, Category
from django.db.models.aggregates import Count

register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    return Category.objects.all()


#  annotate 做的事情就是把全部 Category 取出来，然后去 Post 查询每一个 Category 对应的文章，查询完成后只需算一下每个 category id 对应
# 有多少行记录，这样就可以统计出每个 Category 下有多少篇文章了。把这个统计数字保存到每一条 Category 的记录就
# 可以了（当然并非保存到数据库，在 Django ORM 中是保存到 Category 的实例的属性中，每个实例对应一条记录）。
# 代码中的 Count 方法为我们做了这个事，它接收一个和 Categoty 相关联的模型参数名（这里是 Post，通过 ForeignKey 关联的），然后它
# 便会统计 Category 记录的集合中每条记录下的与之关联的 Post 记录的行数，也就是文章数，最后把这个值保存到 num_posts 属性中
@register.simple_tag
def get_categories():
    # 记得在顶部引入 count 函数
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

