from rest_framework import viewsets
from .models import Pondok, Santri, Pendaftaran
from .serializers import PondokSerializer

class PondokViewSet(viewsets.ModelViewSet):
    queryset = Pondok.objects.all()
    serializer_class = PondokSerializer



