from django.contrib import admin
from .models import Category
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
      prepopulated_fields = {'slug':('title',)}

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
