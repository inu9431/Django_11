from django.db import models
from common.models import Common

class Review(Common):
    content = models.CharField(max_length=120)
    likes_num = models.PositiveIntegerField(default=0)

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    feed = models.ForeignKey("feeds.Feed", on_delete=models.CASCADE)
