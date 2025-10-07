from django.urls import path
from .views import NotificationListView

urlpatterns = [
    # ✅ Endpoint to get user notifications
    path('', NotificationListView.as_view(), name='notifications-list'),
]
