import os
from django.conf import settings
from django.db import models
from colorthief import ColorThief
from webcolors import rgb_to_hex
import PIL

class Album(models.Model):
    title = models.CharField(max_length=256)


class Photo(models.Model):
    def photo_url(self, filename):
        # file will be uploaded to MEDIA_ROOT/photos/<instance.album_id>/<filename>
        return f'photos/{self.album.title}/{filename}'

    def dominant_color(self):
        # getting dominant color of a photo and converting rgb to hex
        path = self.photo.url
        # base_dir = settings.MEDIA_ROOT
        # full_path = os.path.join(base_dir, self.photo.url)
        rgb_color = (ColorThief(f".{path}")).get_color(quality=1)
        hex_color = rgb_to_hex(rgb_color)
        return hex_color

    title = models.CharField(max_length=256)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=photo_url, width_field='photo_width', height_field='photo_height')
    photo_width = models.IntegerField(default=0)
    photo_height = models.IntegerField(default=0)
