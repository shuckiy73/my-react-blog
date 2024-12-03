from django.urls import path
from .views import PostListView, BlogCategoryView, BlogDetailView, BlogFeaturedView, some_view
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='list_view'),
    path('category/<str:category>/', BlogCategoryView.as_view(), name='category'),
    path('featured/', BlogFeaturedView.as_view(), name='featured'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='blog_details'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('some-view/', some_view, name='some_view'),  # Добавляем маршрут для some_view
]