from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views
from . import auth_views

urlpatterns = [
    path('login/', auth_views.login, name='login'),
    path('logout', auth_views.logout, name='logout'),
    path('authenticate/', auth_views.authenticate, name='authenticate'),
    path('signup', auth_views.signup, name='signup'),
    path('signup/submit', auth_views.signup_submit, name='signup_submit'),
    path('users/<str:username>', auth_views.profile, name='profile'),
    path('', views.index),
    path('admin/', admin.site.urls),
    path('blogs/', include('blog.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
