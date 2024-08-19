from djoser.serializers import UserCreateSerializer # type: ignore
from django.contrib.auth import get_user_model
from api.models import UploadedFile
from rest_framework import serializers

User = get_user_model()
class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'name', 'email', 'password', 'username')  
        

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['id', 'title', 'description', 'file', 'visibility', 'cost', 'year_published', 'uploaded_at']