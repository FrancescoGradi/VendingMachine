from django.db import models
from django.utils import timezone

class CoffeeCapsule(models.Model):

    AMERICAN = 'American'
    ARABIC = 'Arabic'
    COFFEE_CHOICES = (
        (AMERICAN, 'American'),
        (ARABIC, 'Arabic'),
    )

    # il campo id e' creato automaticamente ed e' reso chiave primaria
    # i seguenti campi sono spunti soggetti a modifiche o cancellazioni

    coffeeType = models.CharField('Type', choices=COFFEE_CHOICES, max_length=25)
    additionDate = models.DateTimeField('addition date', default=timezone.now)
    expirationDate = models.DateTimeField('expiration date')
    coffeeDescription = models.TextField('Description', max_length=200, help_text="Insert a brief product description")
    coffeePrice = models.DecimalField('Price', max_digits=4, decimal_places=2, default=0.50)
    coffeeQuantity = models.PositiveSmallIntegerField('Quantity', default=1, editable=True)
    coffeeImage = models.ImageField(blank=True, null=True)

    # Funzione per visualizzare meglio il tutto
    def __str__(self):
        return str(self.coffeeType)

    # Se la capsula e' scaduta
    def isExpired(self):
        if self.expirationDate > timezone.now():
            return False
        else:
            return True

    def deleteOneCapsule(self, isLast):
        if self.coffeeQuantity == 1 and isLast:
            self.coffeeQuantity = 0
            self.save()
            return True
        elif self.coffeeQuantity == 1 and not isLast:
            self.delete()
            return True
        elif self.coffeeQuantity > 1:
            self.coffeeQuantity -= 1
            self.save()
            return True
        elif self.coffeeQuantity == 0:
            self.delete()
            return False
        else:
            return False

    # Crea capsule multiple
    @classmethod
    def create(cls, coffeeType, expirationDate, coffeeDescription, coffeePrice, number):
        capsules = list()
        for i in range(number):
            capsules.append(CoffeeCapsule(coffeeType=coffeeType, expirationDate=expirationDate,
                                          coffeeDescription=coffeeDescription, coffeePrice=coffeePrice))
        return capsules

    def addQuantity(self, number):
        self.coffeeQuantity += number
        self.save()

    def empty(self):
        self.coffeeQuantity = 0
        self.save()




