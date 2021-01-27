from django.db import models
from django.db.models.deletion import CASCADE

class Menu(models.Model):
    name = models.CharField(max_length=5)

    class Meta:
        db_table = 'menus'


class Category(models.Model):
    name = models.CharField(max_length=10)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'


class Drink(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    english_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True)
    is_new = models.BooleanField()

    class Meta:
        db_table = 'drinks'


class Image(models.Model):
    url = models.CharField(max_length=1000)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'


class Nutrition(models.Model):
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
    calories = models.CharField(max_length=10)
    saturated_fat = models.CharField(max_length=10)
    protein = models.CharField(max_length=10)
    sodium = models.CharField(max_length=10)
    total_carbs = models.CharField(max_length=10)
    caffeine = models.CharField(max_length=10)

    class Meta:
        db_table = 'nutritions'


class Allergy(models.Model):
    allergen = models.CharField(max_length=10)

    class Meta:
        db_table = 'allergies'


class DrinkAllergy(models.Model):
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
    allergy = models.ForeignKey('Allergy', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'drinks_allergies'
