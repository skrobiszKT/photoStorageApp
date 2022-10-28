from django.db import models
from colorthief import ColorThief
from webcolors import rgb_to_hex


class Photo(models.Model):
    def dominant_color(self):
        # getting dominant color of a photo and converting rgb to hex
        path = self.photo.url
        rgb_color = (ColorThief(f".{path}")).get_color(quality=1)
        hex_color = rgb_to_hex(rgb_color)
        return hex_color

    title = models.CharField(max_length=256)
    albumId = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='photos/', width_field='photo_width', height_field='photo_height')
    url = models.URLField(blank=True)
    photo_width = models.IntegerField(default=0, null=True)
    photo_height = models.IntegerField(default=0, null=True)
    thumbnailUrl = models.URLField(blank=True)
