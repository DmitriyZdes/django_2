from django import template
from django.conf import settings

register = template.Library()


@register.filter()
def media_url(value):
    #if value:
        #return f'/media/products{value}'
    #return '#'

    media_root = settings.MEDIA_URL
    return f"{media_root}{value}"


##@register.simple_tag()
#def mediapath(val):
    #if val:
        #return f'/media/{val}'
    #return '#'
