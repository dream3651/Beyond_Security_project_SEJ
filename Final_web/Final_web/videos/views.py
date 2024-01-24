from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import os
from .utils import apply_model

def index1(request):
    return render(request, 'index1.html')

def next_page1(request, video_url=None):
    return render(request, 'next_page1.html', {'video_url': video_url})

# views.py


def upload_video1(request):
    if request.method == 'POST' and 'video' in request.FILES:
        video = request.FILES['video']
        fs = FileSystemStorage()
        filename = fs.save(video.name, video)
        original_video_url = fs.url(filename)

        processed_video_path = apply_model(fs.path(filename))
        processed_video_url = fs.url(processed_video_path)

        return render(request, 'next_page1.html', {
            'original_video_url': original_video_url,
            'processed_video_url': processed_video_url
        })

    return render(request, 'upload_video1.html')

def news(request):
    return render(request, 'news.html')

def reference(request):
    return render(request, 'reference.html')

