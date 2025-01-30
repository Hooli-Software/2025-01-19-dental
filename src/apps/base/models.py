from django.db import models

from core.models import SingletonModel


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


class SocialAccount(models.Model):
    icon = models.TextField('SVG kodu')
    title = models.CharField('Başlık', max_length=255)
    link = models.URLField('Link')

    class Meta:
        verbose_name = 'Sosyal medya hesabı'
        verbose_name_plural = 'Sosyal medya hesapları'


class FAQ(models.Model):
    question = models.TextField('Soru')
    answer = models.TextField('Cevap')

    class Meta:
        verbose_name = 'Sıkça sorulan soru'
        verbose_name_plural = 'Sıkça sorulan sorular'

    def __str__(self):
        return self.question


class GalleryCategory(models.Model):
    title = models.CharField('Başlık', max_length=128)

    class Meta:
        verbose_name = 'Galeri kategorisi'
        verbose_name_plural = 'Galeri kategorileri'

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    image = models.ImageField('Resim', upload_to='base/gallery-image/image/')
    category = models.ForeignKey(
        GalleryCategory,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='images'
    )

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = 'Galeri resmi'
        verbose_name_plural = 'Galeri resimleri'


class VideoReview(models.Model):
    image = models.ImageField('Resim', upload_to='base/video-review/image/')
    youtube_url = models.URLField('Youtube linki')

    class Meta:
        verbose_name = 'Video değerlendirmesi'
        verbose_name_plural = 'Video değerlendirmeleri'


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
