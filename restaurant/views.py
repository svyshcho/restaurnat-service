from django.views import generic
from django.shortcuts import render
from restaurant.models import Dish, Cook, DishType
from django.contrib.auth.mixins import LoginRequiredMixin


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


class CookerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    template_name = "restaurant/cooker_detail.html"


class PastaListView(generic.ListView):
    queryset = Dish.objects.filter(dish_type__name__icontains="pasta")
    context_object_name = "pasta_list"
    template_name = "restaurant/pasta_list.html"


class PastaDetailView(generic.DetailView):
    model = Dish
    template_name = "restaurant/pasta_detail.html"


class PizzaListView(generic.ListView):
    queryset = Dish.objects.filter(dish_type__name__icontains="pizza")
    context_object_name = "pizza_list"
    template_name = "restaurant/pizza_list.html"


class PizzaDetailView(generic.DetailView):
    model = Dish
    template_name = "restaurant/pizza_detail.html"


class AperitifsListView(generic.ListView):
    queryset = Dish.objects.filter(dish_type__name__icontains="aperitif")
    context_object_name = "aperitifs_list"
    template_name = "restaurant/aperitifs_list.html"


class AperitifsDetailView(generic.DetailView):
    model = Dish
    template_name = "restaurant/aperitifs_detail.html"


class SaladListView(generic.ListView):
    queryset = Dish.objects.filter(dish_type__name__icontains="salad")
    context_object_name = "salads_list"
    template_name = "restaurant/salads_list.html"


class SaladDetailView(generic.DetailView):
    model = Dish
    template_name = "restaurant/salads_detail.html"


class MainDishesListView(generic.ListView):
    queryset = Dish.objects.filter(dish_type__name__icontains="dishes")
    context_object_name = "dish_list"
    template_name = "restaurant/main_dishes_list.html"


class MainDishesDetailView(generic.DetailView):
    model = Dish
    template_name = "restaurant/main_dishes_detail.html"


class DessertsListView(generic.ListView):
    queryset = Dish.objects.filter(dish_type__name__icontains="desserts")
    context_object_name = "desserts_list"
    template_name = "restaurant/desserts_list.html"


class DessertsDetailView(generic.DetailView):
    model = Dish
    template_name = "restaurant/desserts_detail.html"
