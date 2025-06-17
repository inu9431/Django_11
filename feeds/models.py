from django.db import models
from common.models import Common

class Feed(Common):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=120)

    user = models.ForeignKey("users.user", on_delete=models.CASCADE)
