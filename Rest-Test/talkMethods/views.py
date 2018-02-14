from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Talk
from .serializer import TalkSerializer


class TalkViewSet(viewsets.ModelViewSet):
    queryset = Talk.objects.all().order_by('id')
    serializer_class = TalkSerializer