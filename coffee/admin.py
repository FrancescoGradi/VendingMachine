from django.contrib import admin

from .models import CoffeeCapsule

def multipleInsert10(modeladmin, request, queryset):
    capsule = queryset[0]
    capsules = CoffeeCapsule.create(coffeeType=capsule.coffeeType, coffeeDescription=capsule.coffeeDescription,
                                    coffeePrice=capsule.coffeePrice, expirationDate=capsule.expirationDate, number=10)
    for capsule in capsules:
        capsule.save()

def multipleInsert100(modeladmin, request, queryset):
    capsule = queryset[0]
    capsules = CoffeeCapsule.create(coffeeType=capsule.coffeeType, coffeeDescription=capsule.coffeeDescription,
                                    coffeePrice=capsule.coffeePrice, expirationDate=capsule.expirationDate, number=100)
    for capsule in capsules:
        capsule.save()

multipleInsert10.short_description = "Insert 10 multiple istances"
multipleInsert100.short_description = "Insert 100 multiple istances"

class InsertCapsuleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('CoffeeType', {'fields': ['coffeeType']}),
        ('CoffeeDescription', {'fields': ['coffeeDescription']}),
        ('CoffeePrice', {'fields': ['coffeePrice']}),
        ('CoffeeQuantity', {'fields': ['coffeeQuantity']}),
        ('AdditionDate', {'fields': ['additionDate']}),
        ('ExpirationDate', {'fields': ['expirationDate']}),
    ]

    list_display = ('id', 'coffeeType', 'coffeeDescription', 'coffeePrice', 'coffeeQuantity', 'additionDate', 'expirationDate', 'isExpired')
    actions = [multipleInsert10, multipleInsert100]

admin.site.register(CoffeeCapsule, InsertCapsuleAdmin)
