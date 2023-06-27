from django.urls import path, include
from .views import FileUploadAPIView


urlpatterns= [
  path('upload-file/', FileUploadAPIView.as_view(), name='upload-file'),
]