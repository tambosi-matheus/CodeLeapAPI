from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer, ItemPatchSerializer, ItemCreateSerializer
from django.http import Http404

class ItemListCreate(APIView):
    def get(self, request):
        data = Item.objects.all()
        serializer = ItemSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemRetrieveUpdateDestroy(APIView):
    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        instance = self.get_object(pk)
        serializer = ItemSerializer(instance)
        return Response(serializer.data)

    def patch(self, request, pk):
        instance = self.get_object(pk)
        serializer = ItemPatchSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        instance = self.get_object(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

