from rest_framework.serializers import ModelSerializer
from .models import Review
from users.serializers import Feedserializer
class ReviewSerializer(ModelSerializer):
    user = Feedserializer()
    class Meta:
        model = Review
        fields = "__all__"