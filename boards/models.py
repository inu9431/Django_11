from django.db import models
from django.apps import AppConfig

# Create your models here.
# 게시글
#- title
#- content

class Board(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
