from django.shortcuts import get_object_or_404
from django.views.generic.list_detail import object_detail
from recipes.models import Recipe

def detail(request, name):
    recipe = get_object_or_404(Recipe, name__iexact=name)
    return object_detail(
        request, queryset=Recipe.objects.filter(name__iexact=name), slug=name, slug_field='name', template_object_name='recipe'
    )