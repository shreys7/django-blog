from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from .models import Post, Comment
from django.contrib import messages


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blogs/index.html'

def post_detail(request, slug):
    template_name = 'blogs/detail.html'
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        body = request.POST.get('body')

        try:
            comment = Comment.objects.create(
                body=body,
                post=post,
                user=request.user
            )
        except:
            comment = None

        if not comment:
            messages.error(request, 'Could not create comment')
            return redirect_back(request)
        
    comments = post.comments.all()
    return render(request, template_name, {
        'post': post,
        'comments': comments
    })

def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        slug_delimiter = '-'
        try:
            post = Post.objects.create(
                title=title,
                content=content,
                slug=slug_delimiter.join(title.lower().split(' ')),
                author=request.user,
                status=1
            )
        except:
            post = None

        if not post:
            messages.error(request, 'Could not create post')
            return redirect_back(request)
        else:
            messages.success(request, 'Blog was created successfully')
            return redirect('/blogs')
    else:
        return render(request, 'blogs/create_blog.html')

def redirect_back(request):
    return redirect(request.META.get('HTTP_REFERER'))
