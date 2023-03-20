"""View module for handling requests about cases"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from velocityapi.models import Case


class CaseView(ViewSet):
    """Level up cases view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single case
        

        Returns:
            Response -- JSON serialized case
        """
        case = Case.objects.get(pk=pk)
        serializer = CaseSerializer(case)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all cases

        Returns:
            Response -- JSON serialized list of cases
        """
        cases = Case.objects.all()
        serializer = CaseSerializer(cases, many=True)
        return Response(serializer.data)
    
class CaseSerializer(serializers.ModelSerializer):
    """JSON serializer for cases
    """
    class Meta:
        model = Case
        fields = ('id', 'title', "link", "img", "price", "brand", "model", "side_panel", "color", "cabinet_type")

