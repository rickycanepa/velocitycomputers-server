"""View module for handling requests about motherboards"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from velocityapi.models import Motherboard


class MotherboardView(ViewSet):
    """Level up motherboards view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single motherboard
        

        Returns:
            Response -- JSON serialized motherboard
        """
        motherboard = Motherboard.objects.get(pk=pk)
        serializer = MotherboardSerializer(motherboard)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all motherboards

        Returns:
            Response -- JSON serialized list of motherboards
        """
        motherboards = Motherboard.objects.all()
        serializer = MotherboardSerializer(motherboards, many=True)
        return Response(serializer.data)
    
class MotherboardSerializer(serializers.ModelSerializer):
    """JSON serializer for motherboards
    """
    class Meta:
        model = Motherboard
        fields = ('id', 'title', "link", "img", "price", "brand", "model", "form_factor", "chipset", "memory_slots", "socket_type")

