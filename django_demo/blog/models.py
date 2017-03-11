from django.db import models
from django.contrib import admin  # 定义默认的admin站点


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')


admin.site.register(BlogPost, BlogPostAdmin)  # 注册BlogPost model
