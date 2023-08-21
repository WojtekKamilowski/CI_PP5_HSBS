from . import views
from django.urls import path


urlpatterns = [
    path('', views.Posts.as_view(), name="blog"),
    path('add_post/', views.Posts.add_post, name="add_post"),
    path('edit_post/<slug:slug>', views.Posts.edit_post, name="edit_post"),
    path('delete_post/<slug:slug>', views.Posts.delete_post, name="delete_post"),
    path('<slug:slug>/', views.PostDetail.as_view(), name="post_detail"),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
