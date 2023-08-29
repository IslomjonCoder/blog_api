from django.conf.urls.static import static
from django.urls import path

from config import settings
from .views import PostListView, PostDetailView, CommentListView, PostCreateView

urlpatterns = [
    # API views for posts
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', CommentListView.as_view(), name='comment-list'),
    path('posts/create/', PostCreateView.as_view(), name='post-create'),

]

