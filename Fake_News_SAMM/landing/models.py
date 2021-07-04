from django.db import models
from register.models import User

# Create your models here.

class Twitter(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.IntegerField(null=True)
    username = models.CharField(max_length=64, verbose_name="username")
    avatar = models.CharField(default='',max_length=64, verbose_name="profile_picture")
    likes = models.IntegerField(null=True)
    comments = models.IntegerField(null=True)
    pic = models.CharField(max_length=100, verbose_name="image_upload")
    reposts = models.IntegerField(null=True)
    content=models.TextField(max_length=5000,blank=True,verbose_name="content")
    pic = models.ImageField(verbose_name='attached_image',null=True,upload_to='static/images/')
    add_time = models.DateTimeField(verbose_name='publication_date', auto_now_add=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts' 

    @property
    def get_children(self):
        return Comment.objects.filter(tid=self.id).order_by('-id')


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.IntegerField(null=True)
    username = models.CharField(max_length=64, verbose_name="username")
    avatar = models.CharField(default='',max_length=64, verbose_name="profile_picture")
    tid = models.ForeignKey('Twitter', verbose_name='id', null=True, on_delete=models.CASCADE, related_name='parent_tw', default=None)
    content = models.TextField(max_length=5000,blank=True,verbose_name="content")
    add_time = models.DateTimeField(verbose_name='publication_date', auto_now_add=True)
