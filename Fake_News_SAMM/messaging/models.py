from django.db import models

from django.db import models

class message(models.Model):
    time_stamp = models.DateTimeField(verbose_name='publication_date', auto_now_add=True)
    id = models.AutoField(primary_key=True)
    sender_id = models.IntegerField(null=True)
    receiver_id = models.IntegerField(null=True)
    content = models.TextField(max_length=5000,blank=True,verbose_name="content")

