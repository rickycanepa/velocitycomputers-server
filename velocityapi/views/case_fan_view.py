"""View module for handling requests about case fans"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from velocityapi.models import CaseFan


class CaseFanView(ViewSet):
    """Level up case fans view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single case fan
        

        Returns:
            Response -- JSON serialized case fan
        """
        case_fan = CaseFan.objects.get(pk=pk)
        serializer = CaseFanSerializer(case_fan)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all case fans

        Returns:
            Response -- JSON serialized list of case fans
        """
        case_fans = CaseFan.objects.all()
        serializer = CaseFanSerializer(case_fans, many=True)
        return Response(serializer.data)
    
class CaseFanSerializer(serializers.ModelSerializer):
    """JSON serializer for case fans
    """
    class Meta:
        model = CaseFan
        fields = ('id', 'title', "link", "img", "price", "brand", "model", "rpm", "airflow", "noise_level")


