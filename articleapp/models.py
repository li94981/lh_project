from django.db import models


class Pic(models.Model):
    """
    富文本编辑器
    """
    img = models.ImageField(upload_to='static/img')
    upload_time = models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 't_pic'


class Mrticle(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    create_date = models.CharField(max_length=255, blank=True, null=True)
    publish_date = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        db_table = 'article'


