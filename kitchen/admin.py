from django.contrib import admin

from kitchen.models import Dish, DishType


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "dish_type")
    list_filter = ("dish_type",)
    search_fields = ("name",)
    autocomplete_fields = ("dish_type",)
