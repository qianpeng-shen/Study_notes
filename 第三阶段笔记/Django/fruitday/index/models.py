from django.db import models

# Create your models here.
class GoodsType(models.Model):
    title=models.CharField(max_length=30)
    picture=models.ImageField(upload_to='static/upload/goodstype')
    desc=models.CharField(max_length=500)
    def __str__(self):
        return self.title

class Goods(models.Model):
    title=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    spec=models.CharField(max_length=30)
    picture=models.ImageField(upload_to='static/upload/goods')
    isActive=models.BooleanField(default=True)
    #增加GoodsType的引用(1:M)
    goodsType=models.ForeignKey(GoodsType,null=True)
    def __str__(self):
        return self.title

class User(models.Model):
    uphone=models.CharField(max_length=11)
    upwd=models.CharField(max_length=20)
    uemail=models.EmailField(null=True)
    uname=models.CharField(max_length=20)
    isActive=models.BooleanField(default=True)
    def __str__(self):
        return self.uphone


