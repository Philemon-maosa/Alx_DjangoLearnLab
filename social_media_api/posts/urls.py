from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, user_feed

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    # Feed endpoint
    path('feed/', user_feed, name='user-feed'),

    # Include Post and Comment viewsets
    path('', include(router.urls)),
]
