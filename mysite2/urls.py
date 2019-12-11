from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('blogs/', include('blog.urls'))
]
