# accounts/views.py
from rest_framework import generics, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from .serializers import UserRegistrationSerializer

User = get_user_model()

# ------------------------------
# User Registration Endpoint
# ------------------------------
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

# ------------------------------
# Custom Login Endpoint Returning Token
# ------------------------------
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

# ------------------------------
# User Profile Endpoint
# ------------------------------
class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer  # or a dedicated profile serializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

# ------------------------------
# Follow/Unfollow Endpoints
# ------------------------------
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    """
    Authenticated user follows another user.
    """
    try:
        target_user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    if target_user == request.user:
        return Response({"error": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)

    request.user.following.add(target_user)
    return Response({"message": f"You are now following {target_user.username}"})


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    """
    Authenticated user unfollows another user.
    """
    try:
        target_user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    if target_user == request.user:
        return Response({"error": "You cannot unfollow yourself"}, status=status.HTTP_400_BAD_REQUEST)

    request.user.following.remove(target_user)
    return Response({"message": f"You have unfollowed {target_user.username}"})
