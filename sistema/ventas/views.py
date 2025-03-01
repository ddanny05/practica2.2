from django.shortcuts import render
from rest_framework import viewsets
from .models import Clientes
from .serializers import ClienteSerializer
from rest_framework.permissions import AllowAny

# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [AllowAny]

    