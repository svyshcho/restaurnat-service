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


