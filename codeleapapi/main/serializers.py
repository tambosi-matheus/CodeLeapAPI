from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ItemPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['title', 'content']

class ItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['username', 'title', 'content']