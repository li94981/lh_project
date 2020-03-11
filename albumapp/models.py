from django.db import models


# Create your models here.
from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    score = models.CharField(max_length=255,blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    broadcast = models.CharField(max_length=255, blank=True, null=True)
    count = models.CharField(max_length=255,blank=True, null=True)
    brief = models.CharField(max_length=255, blank=True, null=True)
    publish_date = models.CharField(max_length=255,blank=True, null=True)
    cover = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.CharField(max_length=255,blank=True, null=True)

    class Meta:
        db_table = 'album'


class Chapter(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    size = models.CharField(max_length=255, blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    album_id = models.CharField(max_length=36, blank=True, null=True)
    class Meta:
        db_table = 'chapter'
