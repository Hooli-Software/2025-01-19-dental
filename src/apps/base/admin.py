from django.contrib import admin

from . import models


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


@admin.register(models.SocialAccount)
class SocialAccountsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'link'
    )


@admin.register(models.FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'answer'
    )


class GalleryImageTabularInline(admin.TabularInline):
    model = models.GalleryImage


@admin.register(models.GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    inlines = (
        GalleryImageTabularInline,
    )


@admin.register(models.VideoReview)
class VideoReviewAdmin(admin.ModelAdmin):
    list_display = (
        'youtube_url',
    )


@admin.register(models.GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = (
        'image',
    )


@admin.register(models.DoctorInfo)
class DoctorInfoAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'area',
        'slogan'
    )


@admin.register(models.ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = (
        'phone_number_repr',
        'phone_number_wa_repr',
        'email',
        'address'
    )
