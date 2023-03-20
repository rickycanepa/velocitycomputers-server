"""View module for handling requests about processors"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from velocityapi.models import Processor


class ProcessorView(ViewSet):
    """Velocity processors view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single processor
        

        Returns:
            Response -- JSON serialized processor
        """
        processor = Processor.objects.get(pk=pk)
        serializer = ProcessorSerializer(processor)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all processors

        Returns:
            Response -- JSON serialized list of processors
        """
        processors = Processor.objects.all()
        serializer = ProcessorSerializer(processors, many=True)
        return Response(serializer.data)
    
class ProcessorSerializer(serializers.ModelSerializer):
    """JSON serializer for processors
    """
    class Meta:
        model = Processor
        fields = ('id', 'title', "link", "img", "price", "brand", "model", "speed", "socket_type")

