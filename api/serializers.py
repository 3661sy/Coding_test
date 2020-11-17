from rest_framework import serializers
from .models import car, draft, CarPhoto

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhoto
        fields = ['image']

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = car
        fields = ['user', 'accident', 'repair', 'manufacturer', 'price']

class DraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = draft
        fields = [ 'user', 'accident', 'repair', 'manufacturer', 'price']