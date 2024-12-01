from django.db import models

#creation de nootre base de donnee

class Categorie(models.Model):
   name= models.CharField(max_length=250)
   def __str__(self):
        return self.name

#class pour pour les produits

class Produits(models.Model):
    name = models.CharField(max_length= 100)
    Categorie= models.ForeignKey(Categorie, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantite=models.PositiveIntegerField(default=0)
    description= models.TextField()
    date_ajout= models.DateTimeField(auto_now_add=True)
    date_expiration= models.DateField()
    image=models.ImageField(null=True,blank=True, upload_to='media/')

    class Meta:
        ordering =['date_ajout']

    def statut_quantite(self):

        #si la quantite est egale on affiche rouge
        if self.quantite == 0:
            return 'red'
        #sinon si la quantite est superieur ou egael  a 10
        elif self.quantite <= 10 :
            return 'orange'
        else:
            return 'green'
    def __str__(self):
        return self.name
        
        
#creation de la classe utilisateur
class Customer(models.Model):
    name= models.CharField(max_length=100)
    def __str__(self):
        return self.name
        

#CREATION DES MODELS POUR EFFECTUE LA VENTE
class Vente(models.Model):
    produit = models.ForeignKey(Produits, on_delete=models.CASCADE)
    sale_date = models.DateTimeField(auto_now_add=True)
    quantite = models.PositiveIntegerField()
    customer = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.produit

#creation d'une class pour les factures 
class Facture_Client(models.Model):
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    quantite = models.PositiveIntegerField()
    date_achat = models.DateTimeField(auto_now_add=False)
    total_amount  = models.ForeignKey(Vente, on_delete= models.CASCADE)
    produit = models.ForeignKey(Produits, on_delete=models.CASCADE)

    def __str__(self):
        return f"Le recu de {self.customer.customer}"