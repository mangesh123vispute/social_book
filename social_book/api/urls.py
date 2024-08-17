from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register,name='register'),
    path('login/', views.user_login,name='login'),
    path('logout/', views.user_logout,name='logout'),
    path('authors&sellers/', views.authors_sellers,name='authors&sellers'),
    path('upload/', views.upload_file,name='upload'),
    path('uploaded_files/', views.uploaded_files,name='uploaded_files'),
]
