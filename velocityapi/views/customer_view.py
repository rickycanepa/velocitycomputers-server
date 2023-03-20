"""View module for handling requests about customers"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from velocityapi.models import Customer


class CustomerView(ViewSet):
    """customer view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single customer
        

        Returns:
            Response -- JSON serialized customer
        """
        customer = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all customers

        Returns:
            Response -- JSON serialized list of customers
        """
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)
    
class CustomerSerializer(serializers.ModelSerializer):
    """JSON serializer for customers
    """
    class Meta:
        model = Customer
        fields = ('id', 'user', "bio")
        depth = 1


