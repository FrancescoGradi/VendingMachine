from django.contrib import admin

from .models import CoffeeCapsule


class InsertCapsuleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('CoffeeOrigin', {'fields': ['coffeeOrigin']}),
        ('CoffeeType', {'fields': ['coffeeType']}),
        ('AdditionDate', {'fields': ['additionDate']}),
        ('ExpirationDate', {'fields': ['expirationDate']}),
    ]

    list_display = ('id', 'coffeeOrigin', 'coffeeType', 'additionDate', 'expirationDate', 'isExpired')


admin.site.register(CoffeeCapsule, InsertCapsuleAdmin)
