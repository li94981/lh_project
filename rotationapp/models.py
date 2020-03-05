from django.db import models

# Create your models here.

# Create your models here.
class Pic(models.Model):
    title = models.CharField(max_length=100)
    zhuangtai = models.CharField(max_length=100)
    miaoshu = models.TextField()
    datetime = models.DateTimeField(blank=True)
    headpic = models.ImageField(upload_to="pics")
    class Meta:
        db_table="pic"
