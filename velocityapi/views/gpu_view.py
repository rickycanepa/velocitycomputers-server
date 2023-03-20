"""View module for handling requests about gpus"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from velocityapi.models import GPU


class GPUView(ViewSet):
    """Velocity gpus view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single gpu
        

        Returns:
            Response -- JSON serialized gpu
        """
        gpu = GPU.objects.get(pk=pk)
        serializer = GpuSerializer(gpu)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all gpus

        Returns:
            Response -- JSON serialized list of gpus
        """
        gpus = GPU.objects.all()
        serializer = GpuSerializer(gpus, many=True)
        return Response(serializer.data)
    
class GpuSerializer(serializers.ModelSerializer):
    """JSON serializer for cases
    """
    class Meta:
        model = GPU
        fields = ('id', 'title', "link", "img", "price", "brand", "model", "storage_interface", "memory", "clockSpeed", "chipset")

