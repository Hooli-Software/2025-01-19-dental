from django.contrib import admin

from . import models


@admin.register(models.Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


class ServiceTabularInline(admin.TabularInline):
    model = models.Service


@admin.register(models.ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    inlines = (
        ServiceTabularInline,
    )


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


@admin.register(models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'service'
    )


@admin.register(models.SocialAccount)
class SocialAccountsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'link'
    )


@admin.register(models.DoctorInfo)
class DoctorInfoAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'area',
        'paragraph'
    )


@admin.register(models.ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = (
        'phone_number_repr',
        'phone_number_wa_repr',
        'email',
        'address'
    )
