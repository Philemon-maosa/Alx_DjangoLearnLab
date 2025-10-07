from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification

# -------------------------------
# Post ViewSet
# -------------------------------
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# -------------------------------
# Comment ViewSet
# -------------------------------
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# -------------------------------
# Like Post
# -------------------------------
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Check if already liked
    if Like.objects.filter(user=request.user, post=post).exists():
        return Response({'error': 'You already liked this post'}, status=status.HTTP_400_BAD_REQUEST)

    # Create like
    Like.objects.create(user=request.user, post=post)

    # Create notification
    if post.author != request.user:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post"
        )

    return Response({'message': 'Post liked successfully'}, status=status.HTTP_201_CREATED)

# -------------------------------
# Unlike Post
# -------------------------------
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Check if like exists
    like = Like.objects.filter(user=request.user, post=post).first()
    if not like:
        return Response({'error': 'You have not liked this post'}, status=status.HTTP_400_BAD_REQUEST)

    like.delete()
    return Response({'message': 'Post unliked successfully'}, status=status.HTTP_200_OK)

# -------------------------------
# User Feed
# -------------------------------
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_feed(request):
    """
    Returns posts from users that the current user follows.
    """
    following_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
