from django.shortcuts import render

from django.views.generic import ListView

from .models import *

# # Create your views here.
# def home(request):

#     #recuperation de toutes les valeurs quise trouve dans la bade donnees
#     # donnees = Produits.objects.all

#     # context ={
#     #     'donnees':donnees
#     # }

#     return render(request,'home.html',context)


#faisons une autre forme d'affichage fonde sur des class

class Affichage(ListView):
    #affichage du templete 
    template_name= 'home.html'
    #recuperation des info de la Bdd
    queryset = Produits.objects.all()