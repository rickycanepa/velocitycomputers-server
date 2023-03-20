"""velocitycomputers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from velocityapi.views import register_user, login_user
from django.conf.urls import include
from rest_framework import routers
from velocityapi.views import CaseFanView, CaseView, ComputerView, CpuCoolerView, CustomerView, GPUView, KeyboardView, MotherboardView, MouseView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'casefans', CaseFanView, 'casefan')
router.register(r'cases', CaseView, 'case')
router.register(r'computers', ComputerView, 'computer')
router.register(r'cpu_coolers', CpuCoolerView, 'cpu_cooler')
router.register(r'customers', CustomerView, 'customer')
router.register(r'gpus', GPUView, 'gpu')
router.register(r'keyboards', KeyboardView, 'keyboard')
router.register(r'motherboards', MotherboardView, 'motherboard')
router.register(r'mice', MouseView, 'mouse')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
