from django.contrib import admin
from recipes.models import *

admin.site.register(Recipe)
admin.site.register(Style)