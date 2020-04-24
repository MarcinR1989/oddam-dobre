from django.contrib import admin
from .models import CustomUser, Category, Institution, Donation


# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    pass


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    pass
