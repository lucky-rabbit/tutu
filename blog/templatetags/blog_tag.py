#coding:utf-8

from ..models import Post, Category
from django import template

register = template.Library()

#最新文章模板标签
#注册并使用模板标签。Django 1.9 后才支持 simple_tag 模板标签
@register.simple_tag
def get_recent_posts(num=5):
	return Post.objects.all()[:num]

#归档文章模板标签
#dates方法返回一个列表, order='DESC' 降序排列,即离当前越近的时间越排前面
@register.simple_tag
def archives():
	return Post.objects.dates('created_time', 'month', order='DESC')

#分类模板标签
@register.simple_tag
def get_categories():
	return Category.objects.all()