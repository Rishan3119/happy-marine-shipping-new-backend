from rest_framework import serializers
from web.models import RegisterShipForSale,CstmUser,Category,Sub_category,Amenities

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=CstmUser
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_category
        fields = '__all__'

class AmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenities
        fields = '__all__'

class RegSgipForSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterShipForSale
        fields = '__all__'