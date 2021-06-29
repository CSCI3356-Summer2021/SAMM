from django.db import models

# Create your models here.

class UserReport(models.Model):
    REPORTED_PERSON=("{{request.post.author}}")
    username = models.CharField(max_length=7, default=REPORTED_PERSON, editable=False)
    reason = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.username


class MessageReport(models.Model):
    REPORTED_PERSON=("{{request.post.author}}")
    REASONS=(
        ("CH", "Contains Hate Speech"),
        ("CN", "Contains Nudity"),
        ("CFN","Contains Fake News"),
        ("CTTO", "Contains Threats Towards Others"),
        ("OL", "Offensive Language"),
        )
    username = models.CharField(max_length=7, default=REPORTED_PERSON, editable=False)
    reason = models.CharField(max_length=4, choices=REASONS, null=True)
    additional = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.username

