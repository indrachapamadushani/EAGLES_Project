from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    path('follow', views.follow, name='follow'),
    path('profile/<str:pk>',views.profile,name='profile'),
    path('like-post',views.like_post,name = 'like-post'),
]
