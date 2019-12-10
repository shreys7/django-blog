from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('<slug:slug>/', views.Postdetail.as_view(), name='detail')
]