from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('', view=views.posts_list, name="index"),
    path('new/', views.new_post, name="create"),
    path('<slug:slug>', view=views.single_post, name="show"),
    path('<int:pk>/like', view=views.like_post, name="like"),
    path('<int:pk>/bookmark', view=views.bookmark_post, name="bookmark"),
]