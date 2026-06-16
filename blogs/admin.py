from django.contrib import admin
from .models import Category
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
      prepopulated_fields = {'slug':('title',)}
      list_display=('title','category','author','is_featured','status')
      search_fields=('id','title','category__category_name','author__username','status','is_featured')
      list_editable=('status','is_featured')

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
