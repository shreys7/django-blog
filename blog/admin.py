from django.contrib import admin
from .models import Post
from .models import Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on', 'image_src')
    search_fields = ['title', 'content']
    prepoulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'post', 'created_on', 'user')
    list_filter = ('created_on',)
    search_fields = ['body']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
