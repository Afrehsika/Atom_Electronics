from rest_framework import serializers
from periodic_table.serializers import ElementSerializer
from .models import Bond, Material

class BondSerializer(serializers.ModelSerializer):
    element_1_detail = ElementSerializer(source='element_1', read_only=True)
    element_2_detail = ElementSerializer(source='element_2', read_only=True)

    class Meta:
        model = Bond
        fields = '__all__'

class MaterialSerializer(serializers.ModelSerializer):
    bonds = BondSerializer(many=True, read_only=True)

    class Meta:
        model = Material
        fields = '__all__'
