from django.contrib import admin
from recipes.models import *

admin.site.register(Recipe)
admin.site.register(Style)
admin.site.register(Yeast)
admin.site.register(Fermentable)
admin.site.register(Hops)
admin.site.register(Adjunct)
admin.site.register(Ingredient)
admin.site.register(Instructions)