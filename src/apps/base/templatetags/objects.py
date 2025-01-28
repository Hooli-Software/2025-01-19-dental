from django import template

from .. import models

register = template.Library()


@register.simple_tag
def get_service_categories():
    return models.ServiceCategory.objects.all()


@register.simple_tag
def get_services(category_id):
    return models.ServiceCategory.objects.get(id=category_id).services
