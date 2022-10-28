from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.test import TestCase, Client
from photoStorage.models import Photo
from django.urls import reverse
import json
from rest_framework import status

client = Client()


class GetPhotoTest(TestCase):
    # creates photo instance
    def setUp(self):
        ext_url = "https://icons.iconarchive.com/icons/iconka/meow/256/cat-tied-icon.png"
        self.p = Photo()
        self.p.title = "test"
        self.p.albumId = "2"
        self.p.url = ext_url

        r = client.get(ext_url)
        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(r.content)
        img_temp.flush()
        name = ext_url.split("/")[-1]

        self.p.photo.save(name, File(img_temp), save=True)
        self.p.save()

    def test_one_photo_instance_exists(self):
        # tests if Photo instance was created
        photo = Photo.objects.get(title="test")
        self.assertTrue(Photo.objects.all().count() == 1)
        self.assertTrue(photo.albumId == 2)
        self.assertFalse(photo.title == "not_test")

    def test_get_invalid_single_photo(self):
        # tests if instance of invalid pk exists
        r = client.get(reverse('photos-detail', kwargs={"pk": 2}))
        self.assertEqual(r.status_code, status.HTTP_404_NOT_FOUND)
