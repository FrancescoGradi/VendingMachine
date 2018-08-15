from django.db import models
from django.utils import timezone

class CoffeeCapsule(models.Model):

    # il campo id e' creato automaticamente ed e' reso chiave primaria
    # i seguenti campi sono spunti soggetti a modifiche o cancellazioni
    coffeeOrigin = models.CharField(max_length=25)
    coffeeType = models.CharField(max_length=25)
    additionDate = models.DateTimeField('addition coffee date')
    expirationDate = models.DateTimeField('expiration coffee date')

    # Funzione per visualizzare meglio il tutto
    def __str__(self):
        return str(self.id) + " " + str(self.coffeeType)

    # Se la capsula e' scaduta
    def isExpired(self):
        if self.expirationDate > timezone.now():
            return False
        else:
            return True
