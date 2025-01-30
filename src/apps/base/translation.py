from modeltranslation.translator import register, TranslationOptions

from . import models


@register(models.Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )


@register(models.ServiceCategory)
class ServiceCategoryTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )


@register(models.FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = (
        'question',
        'answer'
    )


@register(models.DoctorInfo)
class DoctorInfoTranslationOptions(TranslationOptions):
    fields = (
        'full_name',
        'area',
        'paragraph',
        'logo'
    )


@register(models.GalleryCategory)
class GalleryCategoryTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )
