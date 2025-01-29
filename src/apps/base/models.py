from django.db import models

from core.models import SingletonModel


class Advantage(models.Model):
    icon = models.ImageField('İkon', upload_to='base/advantage/icon/')
    title = models.CharField('Başlık', max_length=128)
    description = models.TextField('Açıklama')

    class Meta:
        verbose_name = 'Avantaj'
        verbose_name_plural = 'Avantajlar'

    def __str__(self):
        return self.title


class ServiceCategory(models.Model):
    title = models.CharField('Başlık', max_length=255)
    image = models.ImageField(
        'Görsel',
        upload_to='base/service-category/image'
    )

    class Meta:
        verbose_name = 'Hizmet kategorisi'
        verbose_name_plural = 'Hizmet kategorileri'

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=128)
    price = models.PositiveIntegerField('Fiyat (USD)')
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='services'
    )

    class Meta:
        verbose_name = 'Hizmet'
        verbose_name_plural = 'Hizmetler'

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    image = models.ImageField('Görsel', upload_to='base/portfolio/image/')
    title = models.CharField('Başlık', max_length=128)
    service = models.ForeignKey(
        Service,
        verbose_name='Hizmet',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Portfoyo'
        verbose_name_plural = 'Portfoyo'

    def __str__(self):
        return self.title


class SocialAccount(models.Model):
    icon = models.TextField('SVG kodu')
    title = models.CharField('Başlık', max_length=255)
    link = models.URLField('Link')

    class Meta:
        verbose_name = 'Sosyal medya hesabı'
        verbose_name_plural = 'Sosyal medya hesapları'


class DoctorInfo(SingletonModel):
    full_name = models.CharField('Adı soyadı', max_length=128)
    area = models.CharField('Uzmanlık alanı', max_length=128)
    paragraph = models.TextField('Kısa paragraf')
    logo = models.ImageField('Logo', upload_to='base/doctor-info/logo/')
    slogan = models.TextField('Slogan')

    class Meta:
        verbose_name = 'Doktor bilgileri'
        verbose_name_plural = 'Doktor bilgileri'


class ContactInfo(SingletonModel):
    phone_number = models.CharField('Telefon numarası', max_length=128)
    phone_number_repr = models.CharField('Telefon numarası (metin)', max_length=128)  # noqa
    phone_number_wa = models.CharField('Whatsapp numarası', max_length=128)
    phone_number_wa_repr = models.CharField('Whatsapp numarası (metin)', max_length=128)  # noqa
    email = models.EmailField('E-posta adresi')
    address = models.TextField('Adres')
    address_gm_src = models.TextField('Google harita iframe linki')

    class Meta:
        verbose_name = 'İletişim bilgileri'
        verbose_name_plural = 'İletişim bilgileri'
