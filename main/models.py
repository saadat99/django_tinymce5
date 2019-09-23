from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User

from tinymce.models import HTMLField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = HTMLField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    # 'Post object' title fix
    def __str__(self):
        return self.title

