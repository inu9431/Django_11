from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import Feedserializer

class FeedSerializer(ModelSerializer):
    user = Feedserializer()
    class Meta:
        model = Feed
        fields = "__all__"
        depth = 1