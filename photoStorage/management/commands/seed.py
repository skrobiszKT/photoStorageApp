import json

import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.management.base import BaseCommand

from photoStorage.models import Photo


def get_photos():
    url = ""
    r = requests.get(url, headers={'Content-Type': 'application/json'})
    photos = r.json()
    return photos


def seed_photos():
    for i in get_photos():
        photo = Photo()
        photo.title = i['title']
        photo.albumId = i["albumId"]
        photo.id = i["id"]
        photo.url = i['url']
        photo.thumbnailUrl = i['thumbnailUrl']
        r = requests.get(i["url"])


        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(r.content)
        img_temp.flush()
        file_name = i["url"].split("/")[-1]

        photo.photo.save(file_name, File(img_temp), save=True)
        photo.save()


def clear_data():
  Photo.objects.all().delete()


class Command(BaseCommand):
  def handle(self, *args, **options):
    seed_photos()
    # clear_data()
    print("completed")
