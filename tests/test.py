import pytest
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from photoStorage.models import Photo


@pytest.mark.parametrize("ext_url", "https://icons.iconarchive.com/icons/iconka/meow/256/cat-tied-icon.png")
@pytest.mark.django_db
def test_adding_with_urls(ext_url, client):
    p = Photo()
    p.title = "test"
    p.albumId = "2"
    p.url = ext_url

    r = client.get(ext_url)
    img_temp = NamedTemporaryFile(delete=True)
    img_temp.write(r.content)
    img_temp.flush()
    name = "test_name"

    p.photo.save(name, File(img_temp), save=True)
    p.save()
    assert Photo.objects.get(title="test")
