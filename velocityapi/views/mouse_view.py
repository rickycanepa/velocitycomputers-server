"""View module for handling requests about mice"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from velocityapi.models import Mouse


class MouseView(ViewSet):
    """Velocity mice view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single mouse
        

        Returns:
            Response -- JSON serialized mice
        """
        mouse = Mouse.objects.get(pk=pk)
        serializer = MouseSerializer(mouse)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all mice

        Returns:
            Response -- JSON serialized list of mice
        """
        mouses = Mouse.objects.all()
        serializer = MouseSerializer(mouses, many=True)
        return Response(serializer.data)
    
class MouseSerializer(serializers.ModelSerializer):
    """JSON serializer for mice
    """
    class Meta:
        model = Mouse
        fields = ('id', 'title', "link", "img", "price", "brand", "model", "tracking_method", "color", "wireless")

