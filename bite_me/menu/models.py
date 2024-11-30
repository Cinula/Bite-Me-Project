from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(unique = True)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name 

class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete.CASCADE)
    name = model.CharField()
    description = model.TextFields()
    price = model.DecimalField(max_digit = 6, decimal_places = 2)
    is_available =
    rating =