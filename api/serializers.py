from rest_framework import serializers
from .models import Pondok, Santri, Pendaftaran

class PondokSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pondok
        fields = ['id', 'name', 'location']

class SantriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Santri
        fields = ['id', 'name', 'age', 'pondok']

class PendaftaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pendaftaran
        fields = ['id', 'santri', 'pondok', 'date_registered']
