from django.conf.urls.defaults import patterns, url, include
from recipes.models import Recipe

'''
urlpatterns = patterns('recipes.views',
    url(r'^/new$', 'new', name='new'),
)
'''
urlpatterns = patterns('django.views.generic.create_update',
    (r'^/new$', 'create_object', {'model':Recipe}),
)