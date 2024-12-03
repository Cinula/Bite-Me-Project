from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(unique = True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name 

class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete.CASCADE)
    name = model.CharField(max_length=200)
    description = model.TextFields()
    price = model.DecimalField(max_digit = 6, decimal_places = 2)
    image = models.ImageField(upload_to='menu/')
    is_available = models.BooleanField(default=True)
    rating = models.DecimalField(max_digit=3,decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name