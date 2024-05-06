from rest_framework import serializers
from .models import Pondok

class PondokSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pondok
        fields = ['id', 'name', 'location']

