from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Item
from main_app import models
# Create your views here.

class ItemList(ListView):
    model = Item

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = '/'
