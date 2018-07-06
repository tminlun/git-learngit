from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)#创建时的时间
    last_updated_time = models.DateTimeField(auto_now=True)#每次修改要更新的时间

    #分辨是哪个模型的对象
    def __str__(self):
        return "<Article: %s>" % self.title#当前对象的title