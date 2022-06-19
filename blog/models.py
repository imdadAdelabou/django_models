from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=200)
    text = models.TextField(blank=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()
