from rest_framework import viewsets
from .models import Element
from .serializers import ElementSerializer

class ElementViewSet(viewsets.ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
