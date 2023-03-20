"""View module for handling requests about computers"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from velocityapi.models import Computer, Favorite, Customer, PowerSupply, Processor, GPU, Motherboard, RAM, Case, CpuCooler, Keyboard, Mouse, SSD
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

        # if "myfavorites" in request.query_params
            # myfavorites = Favorites.objects.filter(customer=person whos logged in)
            # return Response(the serialized favorites)
        if "myfavorites" in request.query_params:
            customer = Customer.objects.get(user=request.auth.user)
            myfavorites = Favorite.objects.filter(customer=request.auth.user)
            serializer = FavoriteSerializer(myfavorites, many=True)
            return Response(serializer.data)
        else:
            computers = Computer.objects.all()
            # Set the `joined` property on every computer
            for computer in computers:
                customer = Customer.objects.get(user=request.auth.user)
                # Check to see if the customer is in the favorites list on the event
                computer.joined =  customer in computer.likes.all()
            serializer = ComputerSerializer(computers, many=True)
            return Response(serializer.data)
    
    def create(self, request):
        customer = Customer.objects.get(user=request.auth.user)
        power_supply = PowerSupply.objects.get(pk=request.data["power_supply"])
        processor = Processor.objects.get(pk=request.data(["processor"]))
        gpu = GPU.objects.get(pk=request.data(["gpu"]))
        motherboard = Motherboard.objects.get(pk=request.data(["motherboard"]))
        ram = RAM.objects.get(pk=request.data(["gpu"]))
        case = Case.objects.get(pk=request.data(["case"]))
        cpu_cooler = CpuCooler.objects.get(pk=request.data("cpu_cooler"))
        keyboard = Keyboard.objects.get(pk=request.data("keyboard"))
        mouse = Mouse.objects.get(pk=request.data("mouse"))
        ssd = SSD.objects.get(pk=request.data("ssd"))

        computer = Computer.objects.create(
            name=request.data["name"],
            description=request.data["description"],
            customer=customer,
            power_supply=power_supply,
            processor=processor,
            gpu=gpu,
            motherboard=motherboard,
            ram=ram,
            case=case,
            cpu_cooler=cpu_cooler,
            keyboard=keyboard,
            mouse=mouse,
            ssd=ssd,
            price=request.data["price"]
        )
        serializer = ComputerSerializer(computer)
        return Response(serializer.data)

    
class ComputerSerializer(serializers.ModelSerializer):
    """JSON serializer for computers
    """
    class Meta:
        model = Computer
        fields = ('id', 'name', "description", "customer", "power_supply", "processor", "gpu", "motherboard", "ram", "case", "cpu_cooler", "keyboard", "mouse", "ssd", "price", "likes", "joined")
        depth = 2

class FavoriteSerializer(serializers.ModelSerializer):

    computer = ComputerSerializer()
    class Meta:
        model = Favorite
        fields = ("computer")