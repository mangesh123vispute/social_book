
from django.urls import path, include
from .views import UserFilesView


urlpatterns = [
    
    path('auth/', include('djoser.urls')),  # Updated line
    path('auth/', include('djoser.urls.jwt')),  # If using JWT authentication
    path('user/files/', UserFilesView.as_view(), name='user-files'),
]