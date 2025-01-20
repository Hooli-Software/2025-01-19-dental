from django.contrib import admin

from . import models


@admin.register(models.Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'link'
    )


@admin.register(models.Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


class ServicePriceValueTabularInline(admin.TabularInline):
    model = models.ServicePriceValue


@admin.register(models.ServicePrice)
class ServicePriceAdmin(admin.ModelAdmin):
    list_display = (
        'service',
        'price',
    )
    list_editable = (
        'price',
    )
    inlines = (
        ServicePriceValueTabularInline,
    )


@admin.register(models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'service'
    )


@admin.register(models.SocialAccounts)
class SocialAccountsAdmin(admin.ModelAdmin):
    list_display = (
        'instagram',
        'facebook',
        'pinterest'
    )


@admin.register(models.DoctorInfo)
class DoctorInfoAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'area',
        'paragraph'
    )
