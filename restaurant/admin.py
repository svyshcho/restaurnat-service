from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from restaurant.models import DishType, Cook, Dish

admin.site.register(DishType)


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("years_of_experience",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("years_of_experience",)}),)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "price", "dish_type"]
    list_filter = ["dish_type__name"]
    search_fields = ["name"]
