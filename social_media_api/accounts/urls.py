from django.urls import path
from .views import UserRegistrationView, CustomAuthToken, UserProfileView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),  # User registration
    path('login/', CustomAuthToken.as_view(), name='login'),             # User login (returns token)
    path('profile/', UserProfileView.as_view(), name='profile'),         # User profile management
]
