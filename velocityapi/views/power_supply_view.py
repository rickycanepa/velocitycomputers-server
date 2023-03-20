"""View module for handling requests about powersupplies"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from velocityapi.models import PowerSupply


class PowerSupplyView(ViewSet):
    """Velocity powersupplies view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single powersupply
        

        Returns:
            Response -- JSON serialized powersupply
        """
        powersupply = PowerSupply.objects.get(pk=pk)
        serializer = PowerSupplySerializer(powersupply)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all powersupplies

        Returns:
            Response -- JSON serialized list of powersupplies
        """
        powersupplies = PowerSupply.objects.all()
        serializer = PowerSupplySerializer(powersupplies, many=True)
        return Response(serializer.data)
    
class PowerSupplySerializer(serializers.ModelSerializer):
    """JSON serializer for powersupplies
    """
    class Meta:
        model = PowerSupply
        fields = ('id', 'title', "link", "img", "price", "brand", "model", "side_panel", "color", "cabinet_type")

