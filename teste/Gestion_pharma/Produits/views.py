from django.shortcuts import render

from .models import *

# Create your views here.
def home(request):

    #recuperation de toutes les valeurs quise trouve dans la bade donnees
    donnees = Produits.objects.all

    context ={
        'donnees':donnees
    }

    return render(request,'home.html',context)