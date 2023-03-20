"""View module for handling requests about SSDs"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from velocityapi.models import SSD


class SsdView(ViewSet):
    """Velocity SSDs view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single SSD
        

        Returns:
            Response -- JSON serialized SSD
        """
        ssd = SSD.objects.get(pk=pk)
        serializer = SsdSerializer(ssd)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all SSDs

        Returns:
            Response -- JSON serialized list of SSDs
        """
        ssd = SSD.objects.all()
        serializer = SsdSerializer(ssd, many=True)
        return Response(serializer.data)
    
class SsdSerializer(serializers.ModelSerializer):
    """JSON serializer for SSDs
    """
    class Meta:
        model = SSD
        fields = ('id', 'title', "link", "img", "price", "brand", "model", "size", "quantity", "type")

