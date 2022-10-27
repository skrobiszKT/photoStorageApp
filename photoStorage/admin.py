from django.contrib import admin
from photoStorage.models import Album, Photo
# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)




admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo)
