from rest_framework import serializers
from .models import Photo
import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile


class PhotoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=2048)
    dominant_color = serializers.SerializerMethodField(read_only=True)
    url = serializers.URLField(required=True)
    local_url = serializers.SerializerMethodField(read_only=True)
    albumId = serializers.IntegerField(required=True)
    photo_width = serializers.IntegerField(read_only=True, default=0)
    photo_height = serializers.IntegerField(read_only=True, default=0)
    thumbnailUrl = serializers.URLField(read_only=True)

    def get_dominant_color(self, obj):
        # gets value from Photo class function dominant_color()
        return obj.dominant_color()

    def get_local_url(self, obj):
        return "." + obj.photo.url

    def create(self, validated_data):
        instance = Photo()

        instance.title = validated_data.get('title')
        instance.albumId = validated_data.get('albumId')
        instance.url = validated_data.get("url")
        instance.thumbnailUrl = validated_data.get("url")

        # saving file from URL in ImageField of Photo model instance
        r = requests.get(validated_data.get("url"))
        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(r.content)
        img_temp.flush()
        name = validated_data.get('title') + "-img"

        instance.photo.save(name, File(img_temp), save=True)
        instance.save()

        return instance

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.albumId = validated_data.get('albumId', instance.albumId)
        instance.url = validated_data.get('url', instance.url)
        instance.thumbnailUrl = validated_data.get("url", instance.thumbnailUrl)
        r = requests.get(validated_data.get("url"))
        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(r.content)
        img_temp.flush()

        instance.photo.save(validated_data.get('title'), File(img_temp), save=True)
        instance.save()
        return instance
