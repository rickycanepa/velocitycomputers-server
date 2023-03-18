from django.db import models
from .customer import Customer

class Computer(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE, related_name='computer_customer') 
    power_supply = models.ForeignKey("PowerSupply", on_delete=models.CASCADE, related_name='computer')
    processor = models.ForeignKey("Processor", on_delete=models.CASCADE, related_name='computer')
    gpu = models.ForeignKey("GPU", on_delete=models.CASCADE, related_name='computer')
    motherboard = models.ForeignKey("Motherboard", on_delete=models.CASCADE, related_name='computer')
    ram = models.ForeignKey("RAM", on_delete=models.CASCADE, related_name='computer')
    case = models.ForeignKey("Case", on_delete=models.CASCADE, related_name='computer')
    cpu_cooler = models.ForeignKey("CpuCooler", on_delete=models.CASCADE, related_name='computer')
    keyboard = models.ForeignKey("Keyboard", on_delete=models.CASCADE, related_name='computer')
    mouse = models.ForeignKey("Mouse", on_delete=models.CASCADE, related_name='computer')
    ssd = models.ForeignKey("SSD", on_delete=models.CASCADE, related_name='computer')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    likes = models.ManyToManyField(Customer, through='Favorite', related_name='computers_favorited')

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value