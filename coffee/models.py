from django.db import models
from django.utils import timezone

class CoffeeCapsule(models.Model):

    AMERICAN = 'American'
    ARABIAN = 'Arabian'
    COFFEE_CHOICES = (
        (AMERICAN, 'American'),
        (ARABIAN, 'Arabian'),
    )

    # il campo id e' creato automaticamente ed e' reso chiave primaria
    # i seguenti campi sono spunti soggetti a modifiche o cancellazioni
    coffeeOrigin = models.CharField('Origin', max_length=25)
    coffeeType = models.CharField('Type', choices=COFFEE_CHOICES, max_length=25)
    additionDate = models.DateTimeField('addition date', default=timezone.now())
    expirationDate = models.DateTimeField('expiration date')
    coffeeDescription = models.TextField('Description', max_length=200, help_text="Insert a brief product description")
    coffeePrice = models.DecimalField('Price', max_digits=4, decimal_places=2, default=0.50)
    coffeeQuantity = models.PositiveSmallIntegerField('Quantity', default=1)

    # Funzione per visualizzare meglio il tutto
    def __str__(self):
        return str(self.id) + " " + str(self.coffeeType)

    # Se la capsula e' scaduta
    def isExpired(self):
        if self.expirationDate > timezone.now():
            return False
        else:
            return True



