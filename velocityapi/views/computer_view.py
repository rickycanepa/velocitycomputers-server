"""View module for handling requests about computers"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status
from velocityapi.models import Computer, Favorite, Customer, PowerSupply, Processor, GPU, Motherboard, RAM, Case, CpuCooler, Keyboard, Mouse, SSD
from django.contrib.auth.decorators import login_required


class ComputerView(ViewSet):
    """Velocity computers view"""


    def retrieve(self, request, pk):
        """Handle GET requests for single computer
        

        Returns:
            Response -- JSON serialized computer
        """
        computer = Computer.objects.get(pk=pk)
        serializer = ComputerSerializer(computer)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all computers, filtered by customer if customer ID is provided in query parameters

        Returns:
            Response -- JSON serialized list of computers
        """
        customer_id = request.query_params.get('customer')
        if customer_id:
            customer_instance = Customer.objects.get(pk=customer_id)
            computers = Computer.objects.filter(customer=customer_instance)
        else:
            computers = Computer.objects.all()

        if "myfavorites" in request.query_params:
            customer = Customer.objects.get(user=request.auth.user)
            myfavorites = Favorite.objects.filter(customer=customer)
            serializer = FavoriteSerializer(myfavorites, many=True)
            return Response(serializer.data)
        else:
            # Set the `joined` property on every computer
            for computer in computers:
                if request.auth.user.is_authenticated:
                    customer = Customer.objects.get(user=request.auth.user)
                    # Check to see if the customer is in the favorites list on the computer
                    computer.joined = customer in computer.likes.all()
                else:
                    computer.joined = False

            serializer = ComputerSerializer(computers, many=True)
            return Response(serializer.data)
    
    def create(self, request):
        customer = Customer.objects.get(user=request.auth.user)
        power_supply = PowerSupply.objects.get(pk=request.data["power_supply"])
        processor = Processor.objects.get(pk=request.data["processor"])
        gpu = GPU.objects.get(pk=request.data["gpu"])
        motherboard = Motherboard.objects.get(pk=request.data["motherboard"])
        ram = RAM.objects.get(pk=request.data["ram"])
        case = Case.objects.get(pk=request.data["case"])
        cpu_cooler = CpuCooler.objects.get(pk=request.data["cpu_cooler"])
        keyboard = Keyboard.objects.get(pk=request.data["keyboard"])
        mouse = Mouse.objects.get(pk=request.data["mouse"])
        ssd = SSD.objects.get(pk=request.data["ssd"])

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
        )
        serializer = ComputerSerializer(computer)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a computer
        
        Return: -- Empty body with 204 status code
        """

        computer = Computer.objects.get(pk=pk)
        computer.name = request.data["name"]
        computer.description = request.data["description"]

        power_supply = PowerSupply.objects.get(pk=request.data["power_supply"])
        processor = Processor.objects.get(pk=request.data["processor"])
        gpu = GPU.objects.get(pk=request.data["gpu"])
        motherboard = Motherboard.objects.get(pk=request.data["motherboard"])
        ram = RAM.objects.get(pk=request.data["ram"])
        case = Case.objects.get(pk=request.data["case"])
        cpu_cooler = CpuCooler.objects.get(pk=request.data["cpu_cooler"])
        keyboard = Keyboard.objects.get(pk=request.data["keyboard"])
        mouse = Mouse.objects.get(pk=request.data["mouse"])
        ssd = SSD.objects.get(pk=request.data["ssd"])
        computer.power_supply=power_supply
        computer.processor=processor
        computer.gpu=gpu
        computer.motherboard=motherboard
        computer.ram=ram
        computer.case=case
        computer.cpu_cooler=cpu_cooler
        computer.keyboard=keyboard
        computer.mouse=mouse
        computer.ssd=ssd
        computer.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True)
    def favorite(self, request, pk):
            """Post request for a user to favorite for a computer"""
        
            customer = Customer.objects.get(user=request.auth.user)
            computer = Computer.objects.get(pk=pk)
            computer.likes.add(customer)
            return Response({'message': 'User added'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['delete'], detail=True)
    def unfavorite(self, request, pk):
            """Delete request for a user to sign up for an event"""
    
            customer = Customer.objects.get(user=request.auth.user)
            computer = Computer.objects.get(pk=pk)
            Favorite.objects.get(customer=customer, computer=computer).delete()
            return Response({'message': 'Gamer removed'}, status=status.HTTP_204_NO_CONTENT)



    
class ComputerSerializer(serializers.ModelSerializer):
    """JSON serializer for computers
    """
    class Meta:
        model = Computer
        fields = ('id', 'name', "description", "customer", "power_supply", "processor", "gpu", "motherboard", "ram", "case", "cpu_cooler", "keyboard", "mouse", "ssd", "price", "likes", "joined")
        depth = 3

class FavoriteSerializer(serializers.ModelSerializer):

    computer = ComputerSerializer()
    class Meta:
        model = Favorite
        fields = ("computer")

    
