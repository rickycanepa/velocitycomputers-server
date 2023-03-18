"""View module for handling requests about case fans"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from velocityapi.models import Case


class CaseView(ViewSet):
    """Level up case fans view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single case fan
        

        Returns:
            Response -- JSON serialized case fan
        """
        case = Case.objects.get(pk=pk)
        serializer = CaseSerializer(case)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all case fans

        Returns:
            Response -- JSON serialized list of case fans
        """
        cases = Case.objects.all()
        serializer = CaseSerializer(cases, many=True)
        return Response(serializer.data)
    
class CaseSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Case
        fields = ('id', 'title', "link", "img", "price", "brand", "model", "side_panel", "color", "cabinet_type")

