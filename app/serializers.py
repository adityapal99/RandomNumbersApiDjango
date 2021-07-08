from app.models import RandomNumbers
from rest_framework.serializers import ModelSerializer

class RandomNumberSerializer(ModelSerializer):
    class Meta:
        model = RandomNumbers
        fields = '__all__'
