"""View module for handling requests about RAM"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from velocityapi.models import RAM


class RamView(ViewSet):
    """Velocity RAM view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single RAM
        

        Returns:
            Response -- JSON serialized RAM
        """
        ram = RAM.objects.get(pk=pk)
        serializer = RamSerializer(ram)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all RAM

        Returns:
            Response -- JSON serialized list of RAM
        """
        ram = RAM.objects.all()
        serializer = RamSerializer(ram, many=True)
        return Response(serializer.data)
    
class RamSerializer(serializers.ModelSerializer):
    """JSON serializer for RAM
    """
    class Meta:
        model = RAM
        fields = ('id', 'title', "link", "img", "price", "brand", "model", "size", "quantity", "type")

