from django.urls import path

from posts.views import PostListView, PostDetail, PostCreateView, like

app_name = 'posts'

urlpatterns = [
    path('detail/<int:pk>/', PostDetail.as_view(), name='detail'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),
    path('like/<int:pk>/', like, name='like'),
]