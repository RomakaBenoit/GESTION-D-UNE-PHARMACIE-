from django.contrib import admin

#affichons nos tables da l'espace administation
from .models import *

admin.site.register(Categorie)
admin.site.register(Produits)
admin.site.register(Vente)
admin.site.register(Facture_Client)
admin.site.register(Customer)


