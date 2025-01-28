from django import template

from .. import models

register = template.Library()


@register.simple_tag
def get_slides():
    return models.Slide.objects.all()
