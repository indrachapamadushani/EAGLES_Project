from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('follow', views.follow, name='follow'),
    path('search', views.follow, name='follow'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', name='like-post'),
    path('singup', views.singup, name='singup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
]
