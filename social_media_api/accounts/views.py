from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserRegistrationSerializer

User = get_user_model()

class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserRegistrationSerializer  # You can create a separate serializer if you want
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users can access

    def get_object(self):
        return self.request.user
