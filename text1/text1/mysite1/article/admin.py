from django.contrib import admin
from .models import Article

# Register your models here.
@admin.register(Article)#装饰器
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id","title","content","created","last_updated_time",)
    ordering = ("id",)

#admin.site.register(Article,ArticleAdmin)