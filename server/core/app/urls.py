from django.urls import path
from .views import FileUploadView, FileListView

urlpatterns = [
    path('api/upload/', FileUploadView.as_view(), name='file-upload'),
    path('api/files/', FileListView.as_view(), name='file-list'),
]
