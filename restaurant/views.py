import time
from django.shortcuts import render
from restaurant.models import Dish, Cook, DishType


def index(request):
    num_dish_types = DishType.objects.all()
    num_dishes = Dish.objects.all()
    num_cookers = Cook.objects.all()

    context = {
        "num_dish_types": num_dish_types,
        "num_dishes": num_dishes,
        "num_cookers": num_cookers,
    }

    return render(request, "restaurant/index.html", context=context)
