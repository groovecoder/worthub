from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Style(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    style = models.ForeignKey(Style)
    cloned_from = models.ForeignKey('self', blank=True, null=True)
    qty = models.IntegerField()

    # alcohol-by-volume; e.g., 4.5
    abv = models.DecimalField(max_digits=2, decimal_places=1)
    # international bittering units; e.g., 18
    ibu = models.IntegerField()

    def __unicode__(self):
        return self.name
    
class Instructions(models.Model):
    recipe = models.ForeignKey(Recipe)
    mash_type = models.CharField(max_length=1, choices=settings.MASH_TYPES)
    text = models.TextField()

class Fermentable(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255, blank=True)
    color = models.DecimalField(max_digits=4, decimal_places=1)
    extract = models.DecimalField(max_digits=3, decimal_places=1)
    moisture = models.DecimalField(max_digits=2, decimal_places=1)

    def __unicode__(self):
        return self.name

class Hops(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255, blank=True)
    alpha = models.DecimalField(max_digits=2, decimal_places=1)

    def __unicode__(self):
        return self.name

class Yeast(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255, blank=True)
    attenuation = models.DecimalField(max_digits=3, decimal_places=1)

    def __unicode__(self):
        return self.name

class Adjunct(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    ingredient = generic.GenericForeignKey()
    mash_type = models.CharField(max_length=1, choices=settings.MASH_TYPES)
    qty = models.DecimalField(max_digits=5, decimal_places=2)
    uom = models.CharField(max_length=2, choices=settings.UOM)
    time = models.IntegerField(blank=True)

    def __unicode__(self):
        return self.ingredient.name    