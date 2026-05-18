from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category
from blogs.models import Blog



def home(request):
      categories=Category.objects.all()
      featured_posts=Blog.objects.filter(is_featured=True,status="published")
      no_featured_posts=Blog.objects.filter(is_featured=False,status="published")
      print(no_featured_posts)


      context={'categories':categories,'featured_posts':featured_posts,'no_featured_posts':no_featured_posts}
      return render(request,'home.html',context)
