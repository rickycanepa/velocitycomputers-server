"""View module for handling requests about keyboards"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from velocityapi.models import Keyboard


class KeyboardView(ViewSet):
    """Velocity keyboards view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single keyboard
        

        Returns:
            Response -- JSON serialized keyboard
        """
        keyboard = Keyboard.objects.get(pk=pk)
        serializer = keyboardSerializer(keyboard)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all keyboards

        Returns:
            Response -- JSON serialized list of keyboards
        """
        keyboards = Keyboard.objects.all()
        serializer = keyboardSerializer(keyboards, many=True)
        return Response(serializer.data)
    
class keyboardSerializer(serializers.ModelSerializer):
    """JSON serializer for keyboards
    """
    class Meta:
        model = Keyboard
        fields = ('id', 'title', "link", "img", "price", "brand", "model", "style", "backlit", "color", "wireless")

