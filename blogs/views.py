from django.shortcuts import render

# Create your views here.
from .models import Category
from .models import Blog
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.db.models import Q



def posts_by_category(request, category_id):
    # Fetch the posts that belongs to the category with the id category_id
    posts = Blog.objects.filter(status='published', category=category_id)
    # Use try/except when we want to do some custom action if the category does not exists
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     # redirect the user to homepage
    #     return redirect('home')
    
    # Use get_object_or_404 when you want to show 404 error page if the category does not exist
    category = get_object_or_404(Category, pk=category_id)

    
    context = {
        'posts': posts,
        'category': category,
    }
    print(context)
    return render(request, 'posts_by_category.html', context)


def blog_detail(request,slug):
    blog=get_object_or_404(Blog,slug=slug,status='published')
    context={
        'blog':blog,
    }
    return render(request,'blog_detail.html',context)

def search(request):
    keyword = request.GET.get('keyword')
    
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='published')
    print(blogs)
    print(keyword)
    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)  
