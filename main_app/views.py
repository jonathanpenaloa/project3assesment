from django.shortcuts import render
from django.views.generic import ListView
from .models import Item
# Create your views here.

class ItemList(ListView):
    model = Item