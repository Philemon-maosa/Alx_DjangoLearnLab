from django.contrib import admin
from django.urls import path, include   # include is needed here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # 👈 this connects your app’s urls.py
]
