from django.urls import path
from .views import (
    UserRegistrationView,
    CustomAuthToken,
    UserProfileView,
    follow_user,
    unfollow_user,
    FollowUserView,
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
]
