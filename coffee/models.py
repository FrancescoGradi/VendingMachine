from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

CLASSIC = 'Classic'
ARABIC = 'Arabic'
COFFEE_CHOICES = (
    (CLASSIC, 'Classic'),
    (ARABIC, 'Arabic'),
)

class CoffeeCapsule(models.Model):

    # il campo id e' creato automaticamente ed e' reso chiave primaria
    # i seguenti campi sono spunti soggetti a modifiche o cancellazioni

    coffeeType = models.CharField('Type', choices=COFFEE_CHOICES, max_length=25)
    additionDate = models.DateTimeField('addition date', default=timezone.now)
    expirationDate = models.DateTimeField('expiration date')
    coffeeDescription = models.TextField('Description', max_length=400, help_text="Insert a brief product description")
    coffeePrice = models.DecimalField('Price', max_digits=4, decimal_places=2, default=0.50)
    coffeeQuantity = models.PositiveSmallIntegerField('Quantity', default=1, editable=True)
    coffeeImage = models.ImageField(blank=True, null=True)

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

    def addQuantity(self, number):
        self.coffeeQuantity += number
        self.save()

    def empty(self):
        self.coffeeQuantity = 0
        self.save()

class History(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hCoffeeType = models.CharField('Type', choices=COFFEE_CHOICES, max_length=25)
    hCoffeePrice = models.DecimalField('Price', max_digits=4, decimal_places=2, default=0.50)
    purchaseTime = models.DateTimeField('Purchase Time', default=timezone.now)

    def clean(self):
        self.delete()


