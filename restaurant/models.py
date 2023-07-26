from django.db import models
from django.contrib.auth.models import AbstractUser


class DishType(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=63)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=2, decimal_places=1)
    dish_type = models.ForeignKey("DishType", on_delete=models.CASCADE)


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(default=1)
    dishes = models.ManyToManyField("Dish", related_name="cookers")

    class Meta:
        verbose_name = "cooker"
        verbose_name_plural = "cookers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"
