from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category
from blogs.models import Blog
from assignments.models import About
from .forms import RegistrationForm
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth



def home(request):
      featured_posts=Blog.objects.filter(is_featured=True,status="published")
      no_featured_posts=Blog.objects.filter(is_featured=False,status="published")
      print(no_featured_posts)
      about=About.objects.get()


      context={'featured_posts':featured_posts,'no_featured_posts':no_featured_posts,'about':about}
      return render(request,'home.html',context)


def register(request):
      if(request.method=='POST'):
            form=RegistrationForm(request.POST)
            if(form.is_valid()):
                  form.save()
                  return redirect('home')
      else:
            form=RegistrationForm()
      context={'form':form}
      return render(request,'register.html',context)

def login(request):
      if(request.method=='POST'):
            form=AuthenticationForm(request,request.POST)
            if form.is_valid():
                 username = form.cleaned_data['username']
                 password = form.cleaned_data['password']

                 User=auth.authenticate(username=username,password=password)
                 if User is not None:
                    auth.login(request, User)
                 return redirect('home')
      else:
            form=AuthenticationForm()
      context={'form':form}
      return render(request,'login.html',context)

def logout(request):
      auth.logout(request)
      return redirect('home')
