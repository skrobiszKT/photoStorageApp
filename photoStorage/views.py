from photoStorage.models import Photo
from .serializers import PhotoSerializer
from rest_framework import generics, mixins, pagination



class PhotoView(generics.ListAPIView):
    # list view
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    # pagination_class = pagination.PageNumberPagination


class CreatePhotoView(mixins.CreateModelMixin, generics.GenericAPIView):
    # create view
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
    # update/delete
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
