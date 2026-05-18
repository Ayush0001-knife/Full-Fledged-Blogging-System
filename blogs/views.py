from django.shortcuts import render

# Create your views here.
from .models import Category
from .models import Blog
from django.http import HttpResponse

def posts_by_category(request,category_id):
      category=Category.objects.get(id=category_id)
      posts=Blog.objects.filter(category=category,status='published')
      context={
            'category':category,
            'posts':posts,
      }
      return render(request,'posts_by_category.html',context)
