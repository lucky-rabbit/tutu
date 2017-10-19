# coding:utf-8

from django.shortcuts import render, get_object_or_404
from .models import Post, Category
import markdown
from comments.forms import CommentsForm

def index(request):
	post_list = Post.objects.all()
	context = {'post_list': post_list}
	return render(request, 'blog/index.html', context )

def detail(request, pk):
	#作用是当传入的 pk对应的 Post在数据库存在时返回post; 如果不存在，返回404
	post = get_object_or_404(Post, pk=pk)

	#导入markdown这样我们在模板中展示 {{ post.body }} 就是渲染过后的 HTML 文本
	#传递的额外参数 extensions是对 Markdown 语法的拓展
	#extra 本身包含很多拓展、 codehilite 是语法高亮拓展、toc 允许我们自动生成目录
	post.body = markdown.markdown(post.body,
								 extensions=[
								 	'markdown.extensions.extra',
								 	'markdown.extensions.codehilite',
								 	'markdown.extensions.toc',
								 	])
	form = CommentsForm()
	comments_list = post.comments_set.all()
	context = {'post': post,
				'form':form,
				'comments_list':comments_list
			}
	return render(request, 'blog/detail.html', context)

#created_time 是 Python 的 date 对象。这里作为函数的参数列表，所以 Django 要求写成两个下划线，即 created_time__year
#由于归档下的文章列表的显示和首页是一样的，因此直接渲染index.html 模板
def archives(request, year, month):
	post_list = Post.objects.filter(created_time__year=year,
									created_time__month=month
									)
	context = {'post_list': post_list}
	return render(request, 'blog/index.html', context)

def category(request, pk):
	cate = get_object_or_404(Category, pk=pk)
	post_list = Post.objects.filter(category=cate)
	context = {'post_list': post_list}
	return render(request, 'blog/index.html', context)