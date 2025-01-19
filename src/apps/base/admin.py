from django.contrib import admin

from . import models


@admin.register(models.Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
