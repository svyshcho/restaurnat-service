from django.urls import path

from restaurant.views import (index,
                              PastaListView,
                              PastaDetailView,
                              CookerDetailView,
                              PizzaListView,
                              PizzaDetailView,
                              AperitifsListView,
                              AperitifsDetailView,
                              SaladListView,
                              SaladDetailView,
                              MainDishesListView,
                              MainDishesDetailView,
                              DessertsListView,
                              DessertsDetailView,
                              )

urlpatterns = [
    path("", index, name="index"),
    path("cooker/<int:pk>/", CookerDetailView.as_view(), name="cooker-detail"),
    path("pasta/", PastaListView.as_view(), name="pasta-list"),
    path("pasta/<int:pk>/", PastaDetailView.as_view(), name="pasta-detail"),
    path("pizza/", PizzaListView.as_view(), name="pizza-list"),
    path("pizza/<int:pk>/", PizzaDetailView.as_view(), name="pizza-detail"),
    path("aperitifs/", AperitifsListView.as_view(), name="aperitifs-list"),
    path("aperitifs/<int:pk>/", AperitifsDetailView.as_view(), name="aperitifs-detail"),
    path("salads/", SaladListView.as_view(), name="salad-list"),
    path("salads/<int:pk>/", SaladDetailView.as_view(), name="salad-detail"),
    path("dishes/", MainDishesListView.as_view(), name="main-dishes-list"),
    path("dishes/<int:pk>/", MainDishesDetailView.as_view(), name="main-dishes-detail"),
    path("desserts/", DessertsListView.as_view(), name="desserts-list"),
    path("deserts/<int:pk>/", DessertsDetailView.as_view(), name="desserts-detail"),

]

app_name = "catalog"
