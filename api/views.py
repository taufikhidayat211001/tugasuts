from rest_framework import viewsets
from .models import Pondok, Santri, Pendaftaran
from .serializers import PondokSerializer, SantriSerializer, PendaftaranSerializer

class PondokViewSet(viewsets.ModelViewSet):
    queryset = Pondok.objects.all()
    serializer_class = PondokSerializer

class SantriViewSet(viewsets.ModelViewSet):
    queryset = Santri.objects.all()
    serializer_class = SantriSerializer

class PendaftaranViewSet(viewsets.ModelViewSet):
    queryset = Pendaftaran.objects.all()
    serializer_class = PendaftaranSerializer

