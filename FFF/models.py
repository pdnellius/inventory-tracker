from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ItemType(models.Model):
    name = models.CharField(max_length=128, db_index=True)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    tags = models.ManyToManyField(Category)


class Category(models.Model):
    name = models.CharField(max_length=32, db_index=True)


class Item(models.Model):
    id = models.CharField(max_length=32, unique=True, db_index=True)
    item_type = models.ForeignKey('ItemType', null=False, blank=False)
    location = models.CharField(max_length=128)  # TODO
    quantity = models.IntegerField()
    date_bought = models.DateField(auto_now_add=True)
    date_consumed = models.DateField()
