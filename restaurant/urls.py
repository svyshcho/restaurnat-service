from django.urls import path

from restaurant.views import index, PastaListView, PastaDetailView, CookerDetailView

urlpatterns = [
    path("", index, name="index"),
    path("cooker/<int:pk>/", CookerDetailView.as_view(), name="cooker-detail"),
    path("pasta/", PastaListView.as_view(), name="pasta-list"),
    path("pasta/<int:pk>", PastaDetailView.as_view(), name="pasta-detail"),
]

app_name = "catalog"
