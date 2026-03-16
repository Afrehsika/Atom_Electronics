from rest_framework import viewsets
from .models import Bond, Material
from .serializers import BondSerializer, MaterialSerializer

class BondViewSet(viewsets.ModelViewSet):
    queryset = Bond.objects.all()
    serializer_class = BondSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
