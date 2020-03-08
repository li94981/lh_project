from django.db import models

# Create your models here.
class Usermaster(models.Model):
    shouji_num = models.CharField(max_length=100)
    account = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    header_pic = models.ImageField(upload_to="pics")
    faming = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    addr = models.CharField(max_length=100)
    qianming = models.TextField()
    zhuangtai = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    zhuce_time = models.DateField(blank=True)
    class Meta:
        db_table="t_users"
