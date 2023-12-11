from django.urls import path
from .views import YouTubeDownloader

urlpatterns = [
    path('home/', YouTubeDownloader.as_view(), name='home'),
]