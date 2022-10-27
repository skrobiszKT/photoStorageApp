from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from photoStorage.models import Photo


# Create your views here.
class ColorView(View):
    def get(self, request, pk):
        p = Photo.objects.get(id=pk)
        color = p.dominant_color()
        return HttpResponse(color)