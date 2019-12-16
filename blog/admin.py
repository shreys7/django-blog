from django.contrib import admin
from .models import Post
from .models import Comment

def make_published(self, request, queryset):
    rows_updated = queryset.update(status = 1)
    if rows_updated == 1:
        message_bit = "1 story was"
    else:
        message_bit = "%s stories were" % rows_updated
    self.message_user(request, "%s successfully marked as published." % message_bit)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'image_src')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepoulated_fields = {'slug': ('title',)}
    actions = [make_published]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'post', 'created_on', 'user')
    list_filter = ('created_on',)
    search_fields = ['body']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
