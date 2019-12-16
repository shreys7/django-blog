from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login(request):
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect_back(request)


def authenticate(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(request, username=username, password=password)
    if not user:
        messages.error(request, 'Invalid username/password')
        return redirect_back(request)

    auth.login(request, user)
    messages.info(request, 'You are now logged in as {}.'.format(username))
    return redirect('/blogs')


def signup(request):
    return render(request, 'signup.html')


def signup_submit(request):
    # Get the form data from the request.
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')

    # Validate username is not already taken.
    if User.objects.filter(username=username).exists():
        messages.error(
            request, 'Username {} is already taken.'.format(username))
        return redirect_back(request)

    # Validate email is not already taken.
    if User.objects.filter(email=email).exists():
        messages.error(
            request, 'User with email {} already exists.'.format(email))
        return redirect_back(request)

    if not password == confirm_password:
        messages.error(request, 'Passwords don\'t match')
        return redirect_back(request)

    try:
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
    except:
        user = None

    if not user:
        messages.error(request, 'Error creating a new user.')
        return redirect_back(request)

    messages.info(request, 'User has been created, you can login now.')
    return redirect('/login')

def profile(request, username):
    user = request.user
    blog_posts = user.blog_posts.all()
    template_name = 'profile.html'

    return render(request, template_name, {
        'blog_posts': blog_posts
    })

def redirect_back(request):
    return redirect(request.META.get('HTTP_REFERER'))
