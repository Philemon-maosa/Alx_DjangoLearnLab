from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from notifications.models import Notification
from .serializers import UserSerializer

User = get_user_model()

# ✅ User registration view
class UserRegistrationView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "user": UserSerializer(user).data,
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ Login view using token authentication
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'user_id': token.user_id,
            'email': token.user.email
        })


# ✅ Profile view for logged-in user
class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


# ✅ Follow/unfollow endpoints (simple functions)
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    try:
        user_to_follow = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    if user_to_follow == request.user:
        return Response({'error': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)

    if user_to_follow in request.user.following.all():
        return Response({'message': 'Already following this user'}, status=status.HTTP_400_BAD_REQUEST)

    request.user.following.add(user_to_follow)
    Notification.objects.create(
        recipient=user_to_follow,
        actor=request.user,
        verb="started following you"
    )
    return Response({'message': f'You are now following {user_to_follow.username}'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    try:
        user_to_unfollow = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    if user_to_unfollow not in request.user.following.all():
        return Response({'message': 'You are not following this user'}, status=status.HTTP_400_BAD_REQUEST)

    request.user.following.remove(user_to_unfollow)
    return Response({'message': f'You have unfollowed {user_to_unfollow.username}'}, status=status.HTTP_200_OK)


# ✅ Generic Follow view (toggle follow/unfollow)
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if user_to_follow == request.user:
            return Response({'error': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)

        if user_to_follow in request.user.following.all():
            request.user.following.remove(user_to_follow)
            return Response({'message': 'Unfollowed successfully'}, status=status.HTTP_200_OK)
        else:
            request.user.following.add(user_to_follow)
            Notification.objects.create(
                recipient=user_to_follow,
                actor=request.user,
                verb="started following you"
            )
            return Response({'message': 'Followed successfully'}, status=status.HTTP_201_CREATED)
