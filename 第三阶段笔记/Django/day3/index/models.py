from django.db import models
#声明自定义的 objects-models.Manager
class AuthorManager(models.Manager):
    #添加自定义函数- 查询Author表中共有多少条数据
    def auCount(self):
        return self.all().count()
    def ltage(self,age):
        return self.filter(age__lt=age)
class BookManager(models.Manager):
    def titlecontains(self,keys):
        return self.filter(title__contains=keys)



# Create your models here.
class Publisher(models.Model):
    name=models.CharField(max_length=30,verbose_name='名字')
    address=models.CharField(max_length=50,verbose_name="地址")
    city=models.CharField(max_length=30,verbose_name="出版城市")
    country=models.CharField(max_length=30,verbose_name="国家")
    website=models.URLField(verbose_name="网址")
    def __str__(self):
        return self.name
    class Meta:
        db_table='publisher'
        verbose_name_plural='出版社'

class Book(models.Model):
    objects=BookManager()
    title=models.CharField(max_length=50,verbose_name='书名')
    publicate_date=models.DateField(verbose_name='出版时间')
    #增加对Publisher的引用
    publisher=models.ForeignKey(Publisher,verbose_name='出版社',null=True)
    def __str__(self):
        return self.title
    class Meta:
        db_table='book'
        verbose_name_plural='书籍'
        ordering=['-publicate_date']

class Author(models.Model):
    #使用AuthorManager覆盖当前的objects
    objects=AuthorManager()
    name=models.CharField(max_length=30,verbose_name='名字')
    age=models.IntegerField(verbose_name="年龄")
    email=models.EmailField(null=True,verbose_name="邮件")
    #增加一个列，表示用户是禁用还是启用
    isActive=models.BooleanField(default=True,verbose_name='状态')
    book=models.ManyToManyField(Book)
    publisher=models.ManyToManyField(Publisher)

    def __str__(self):
        return self.name
    #声明内部类，来定义当期那类在管理页面中的展现形式
    class Meta:
        #修改当前表名
        db_table='author'
        #修改实体类在后台管理页的名称(单数)
        verbose_name='作者'
        #修改实体类在后台管理页的名称(复数)
        verbose_name_plural=verbose_name
        #首先按照年龄降序排序，其次按照id升序排序
        ordering=['-age','id']

class Wife(models.Model):
    names=models.CharField(max_length=30)
    age=models.IntegerField()
    #增加一个一对一的引用,引用自Author实体
    author=models.OneToOneField(Author,null=True)


    def __str__(self):
        return self.names

    class Meta:
        db_table='wife'
        verbose_name='夫人'
        verbose_name_plural=verbose_name    


