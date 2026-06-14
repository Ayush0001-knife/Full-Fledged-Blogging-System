from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category
from blogs.models import Blog



def home(request):
      featured_posts=Blog.objects.filter(is_featured=True,status="published")
      no_featured_posts=Blog.objects.filter(is_featured=False,status="published")
      print(no_featured_posts)


      context={'featured_posts':featured_posts,'no_featured_posts':no_featured_posts}
      return render(request,'home.html',context)
