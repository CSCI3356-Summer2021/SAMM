from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField(blank = True, null = True)
    image = models.FileField(upload_to='', blank = True, null = True)
    pub_date = models.DateTimeField('date published')