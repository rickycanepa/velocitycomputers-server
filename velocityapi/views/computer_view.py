"""View module for handling requests about computers"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from velocityapi.models import Computer, Favorite
from django.contrib.auth.decorators import login_required


class ComputerView(ViewSet):
    """Level up computers view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single computer
        

        Returns:
            Response -- JSON serialized computer
        """
        computer = Computer.objects.get(pk=pk)
        serializer = ComputerSerializer(computer)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all computers

        Returns:
            Response -- JSON serialized list of computers
        """

        computers = []

        # if "myfavorites" in request.query_params
            # myfavorites = Favorites.objects.filter(customer=person whos logged in)
            # return Response(the serialized favorites)
        if "myfavorites" in request.query_params:
            myfavorites = Favorite.objects.filter(customer=request.user)
            serializer = FavoriteSerializer()

        computers = Computer.objects.all()
        # Set the `joined` property on every event
        for computer in computers:
            # Check to see if the customer is in the favorites list on the event
            computer.joined =  customer in computer.likes.all()
        serializer = ComputerSerializer(computers, many=True)
        return Response(serializer.data)
                           
    
class ComputerSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Computer
        fields = ('id', 'name', "description", "customer", "power_supply", "processor", "gpu", "motherboard", "ram", "case", "cpu_cooler", "keyboard", "mouse", "ssd", "price", "likes", "joined")
        depth = 1

class FavoriteSerializer(serializers.ModelSerializer):

    computer = ComputerSerializer()
    class Meta:
        model = Favorite
        fields = ("computer")