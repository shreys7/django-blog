from django.contrib import admin
from django.urls import path, include
from .import views
from . import auth_views

urlpatterns = [
    path('login/', auth_views.login, name='login'),
    path('authenticate/', auth_views.authenticate, name='authenticate'),
    path('', views.index),
    path('admin/', admin.site.urls),
    path('blogs/', include('blog.urls'))
]
