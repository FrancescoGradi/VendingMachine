from django.contrib import admin

from .models import CoffeeCapsule


class InsertCapsuleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('CoffeeOrigin', {'fields': ['coffeeOrigin']}),
        ('CoffeeType', {'fields': ['coffeeType']}),
        ('CoffeeDescription', {'fields': ['coffeeDescription']}),
        ('CoffeePrice', {'fields': ['coffeePrice']}),
        ('CoffeeQuantity', {'fields': ['coffeeQuantity']}),
        ('AdditionDate', {'fields': ['additionDate']}),
        ('ExpirationDate', {'fields': ['expirationDate']}),
    ]

    list_display = ('id', 'coffeeOrigin', 'coffeeType', 'coffeeDescription', 'coffeePrice', 'coffeeQuantity', 'additionDate', 'expirationDate', 'isExpired')


admin.site.register(CoffeeCapsule, InsertCapsuleAdmin)
