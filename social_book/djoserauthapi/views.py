from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from api.models import UploadedFile
from .serializers import UploadedFileSerializer

class UserFilesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        uploaded_files = UploadedFile.objects.filter(user=user)

        if not uploaded_files.exists():
            return Response({"detail": "No files found for this user."}, status=status.HTTP_404_NOT_FOUND)

        serializer = UploadedFileSerializer(uploaded_files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

