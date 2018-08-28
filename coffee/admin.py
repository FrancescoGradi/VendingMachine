from django.contrib import admin

from .models import CoffeeCapsule

def add10(modeladmin, request, queryset):
    for capsule in queryset:
        capsule.addQuantity(10)

def add100(modeladmin, request, queryset):
    for capsule in queryset:
        capsule.addQuantity(100)

def emptyCapsules(modeladmin, request, queryset):
    for capsule in queryset:
        capsule.empty()

add10.short_description = "Add 10 capsules"
add100.short_description = "Add 100 capsules"
emptyCapsules.short_description = "Empty capsules"

class InsertCapsuleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('CoffeeType', {'fields': ['coffeeType']}),
        ('CoffeeDescription', {'fields': ['coffeeDescription']}),
        ('CoffeePrice', {'fields': ['coffeePrice']}),
        ('CoffeeQuantity', {'fields': ['coffeeQuantity']}),
        ('Image', {'fields': ['coffeeImage']}),
        ('AdditionDate', {'fields': ['additionDate']}),
        ('ExpirationDate', {'fields': ['expirationDate']}),
    ]

    list_display = ('id', 'coffeeType', 'coffeeDescription', 'coffeePrice', 'coffeeQuantity', 'additionDate', 'expirationDate', 'isExpired')
    actions = [add10, add100, emptyCapsules]

admin.site.register(CoffeeCapsule, InsertCapsuleAdmin)
