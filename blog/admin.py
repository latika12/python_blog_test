from django.contrib import admin

# Register your models here.

from blog.models import Post, Author, Tag, Category

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Category)
