from django.urls import path

from restaurant.views import index, PastaListView, PastaDetailView

urlpatterns = [
    path("", index, name="index"),
    path("pasta/", PastaListView.as_view(), name="pasta-list"),
    path("pasta/<int:pk>", PastaDetailView.as_view(), name="pasta-detail"),
]

app_name = "catalog"
