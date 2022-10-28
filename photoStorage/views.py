from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from photoStorage.models import Photo
from .serializers import PhotoSerializer
from rest_framework import generics, mixins
import requests


# Create your views here.
class ColorView(View):
    def get(self, request, pk):
        p = Photo.objects.get(id=pk)
        color = p.dominant_color()
        return HttpResponse(color)


class PhotoView(generics.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class CreatePhotoView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PhotoDetailView(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# def get_photos(request):
#     all_photos = {}
#
#     url = 'https://jsonplaceholder.typicode.com/photos'
#     response = requests.get(url)
#     data = response.json()
#
#     for photo in data:
#         photo_data = Photo(
#             title = photo['title'],
#             albumId = photo['albumId'],
#             id = photo['id'],
#             url = photo['url'],
#             thumbnailUrl = photo['thumbnailUrl'],
#
#         )
#         photo_data.save()
#         all_photos = Photo.objects.all().order_by('-id')
#
#     return HttpResponse(all_photos)
#
# get_photos(request)