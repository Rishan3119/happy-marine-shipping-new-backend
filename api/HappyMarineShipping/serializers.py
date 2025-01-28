from rest_framework import serializers
from web.models import RegisterShipForSale

class RegSgipForSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterShipForSale
        fields = '__all__'