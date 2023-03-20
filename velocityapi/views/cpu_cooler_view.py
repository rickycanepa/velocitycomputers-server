"""View module for handling requests about cpu coolers"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from velocityapi.models import CpuCooler


class CpuCoolerView(ViewSet):
    """Velocity cpu cooler view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single cpu cooler
        

        Returns:
            Response -- JSON serialized cpu cooler
        """
        cpu_cooler = CpuCooler.objects.get(pk=pk)
        serializer = CpuCoolerSerializer(cpu_cooler)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all cpu coolers

        Returns:
            Response -- JSON serialized list of cpu coolers
        """
        cpu_cooler = CpuCooler.objects.all()
        serializer = CpuCoolerSerializer(cpu_cooler, many=True)
        return Response(serializer.data)
    
class CpuCoolerSerializer(serializers.ModelSerializer):
    """JSON serializer for cpu coolers
    """
    class Meta:
        model = CpuCooler
        fields = ('id', 'title', "link", "img", "price", "brand", "model", "is_water_cooled", "rpm", "color", "noise_level")


