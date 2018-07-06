from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)#参数为添加时的时间,改或添加时不会变动
    last_updated_time = models.DateTimeField(auto_now=True)#参数为你改或添加时间为你现在改的时间

    #标注后台的哪个模型的具体对象
    def __str__(self):
        return "<Article: %s>" % self.title