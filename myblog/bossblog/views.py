from django.shortcuts import render
from django.views import View
from .models import Blog, Category, Tag

from django.http import HttpResponse

from pure_pagination import Paginator, PageNotAnInteger
import markdown

# Create your views here.


class IndexView(View):
    """首页"""
    def get(self, request):

        all_blog = Blog.objects.all().order_by('-id')
        for blog in all_blog:
            blog.content = markdown.markdown(blog.content)
        blog_nums = Blog.objects.count()
        category_nums = Category.objects.count()
        tag_nums = Tag.objects.count()
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_blog, 5, request=request)  # 5为每页展示的博客数目
        all_blog = p.page(page)

        return render(request, 'index.html', {
            'all_blog': all_blog,
            'blog_nums': blog_nums,
            'category_nums ': category_nums,
            'tag_nums ': tag_nums,

        })


class ArichiveView(View):
    def get(self, request):
        all_blog = Blog.objects.all().order_by('-create_time')
        blog_nums = Blog.objects.count()
        category_nums = Category.objects.count()
        tag_nums = Tag.objects.count()
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_blog, 5, request=request)  # 5为每页展示的博客数目
        all_blog = p.page(page)

        return render(request, 'archive.html', {
            'all_blog': all_blog

        })


class TagView(View):
    def get(self, request):
        all_tag = Tag.objects.all()
        blog_nums = Blog.objects.count()
        category_nums = Category.objects.count()
        tag_nums = Tag.objects.count()
        return render(request, 'tags.html',{
            'all_tag': all_tag,

        })


class TagDetailView(View):
    def get(self, request, tag_name):
        tag = Tag.objects.filter(name=tag_name).first()
        tag_blogs = tag.blog_set.all()
        blog_nums = Blog.objects.count()
        category_nums = Category.objects.count()
        tag_nums = Tag.objects.count()
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(tag_blogs, 5, request=request)
        tag_blogs = p.page(page)
        return render(request, 'tag-detail.html', {
            'tag_blogs': tag_blogs,
            'tag_name': tag_name,
            'blog_nums': blog_nums,
            'category_nums ': category_nums,
            'tag_nums ': tag_nums,

        })



class BlogDetailView(View):
    """
    博客详情页
    """
    def get(self, request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        blog.content = markdown.markdown(blog.content)
        blog_nums = Blog.objects.count()
        category_nums = Category.objects.count()
        tag_nums = Tag.objects.count()
        # 实现博客上一篇与下一篇功能
        has_prev = False
        has_next = False
        id_prev = id_next = int(blog_id)
        blog_id_max = Blog.objects.all().order_by('-id').first()
        id_max = blog_id_max.id
        while not has_prev and id_prev >= 1:
            blog_prev = Blog.objects.filter(id=id_prev - 1).first()
            if not blog_prev:
                id_prev -= 1
            else:
                has_prev = True
        while not has_next and id_next <= id_max:
            blog_next = Blog.objects.filter(id=id_next + 1).first()
            if not blog_next:
                id_next += 1
            else:
                has_next = True

        # 将状态码与上下博客传递给前端页面
        # 'blog_prev': blog_prev,
        # 'blog_next': blog_next,
        # 'has_prev': has_prev,
        # 'has_next': has_next,


        return render(request, 'blog-detail.html', {
            'blog': blog,
            'blog_prev': blog_prev,
            'blog_next': blog_next,
            'has_prev': has_prev,
            'has_next': has_next,
            'blog_nums': blog_nums,
            'category_nums ': category_nums,
            'tag_nums ': tag_nums,

        })








