from django.db import models

from core.models import SingletonModel


class Slide(models.Model):
    CHOICES_TYPE = (
        ('1', 'FIRST'),
        ('2', 'SECOND'),
        ('3', 'THIRD')
    )

    title = models.CharField('Başlık', max_length=128)
    subtitle = models.CharField('Alt başlık', max_length=128)
    image = models.ImageField('Görsel', upload_to='base/slide/image/')
    type = models.CharField(choices=CHOICES_TYPE, max_length=12)

    # non-required fields
    show_button = models.BooleanField('Buton gösterilsinmi?', default=False)
    button_text = models.CharField('Buton metni', max_length=36, blank=True, null=True)  # noqa
    button_link = models.URLField('Link', blank=True, null=True)

    class Meta:
        verbose_name = 'Stayt'
        verbose_name_plural = 'Slaytlar'

    def __str__(self):
        return self.title


class Advantage(models.Model):
    icon = models.ImageField('İkon', upload_to='base/advantage/icon/')
    title = models.CharField('Başlık', max_length=128)
    description = models.TextField('Açıklama')

    class Meta:
        verbose_name = 'Avantaj'
        verbose_name_plural = 'Avantajlar'

    def __str__(self):
        return self.title


class Service(models.Model):
    icon = models.ImageField(
        'Görsel',
        upload_to='base/service/icon/',
        blank=True,
        null=True
    )
    title = models.CharField(max_length=128)
    description = models.TextField()

    class Meta:
        verbose_name = 'Hizmet'
        verbose_name_plural = 'Hizmetler'

    def __str__(self):
        return self.title


class ServicePrice(models.Model):
    service = models.ForeignKey(
        Service,
        verbose_name='Hizmet',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    price = models.PositiveIntegerField('Fiyat')
    message = models.TextField('Mesaj', blank=True, null=True)

    class Meta:
        verbose_name = 'Hizmet fiyatı'
        verbose_name_plural = 'Hizmet fiyatları'

    def __str__(self):
        return f'#{self.id} - {self.service} ({self.price})'


class ServicePriceValue(models.Model):
    title = models.CharField('Başlık', max_length=128)
    is_included = models.BooleanField('Dahilmidir?', default=True)
    service_price = models.ForeignKey(
        ServicePrice,
        verbose_name='Hizmet fiyatı',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Hizmet fiyatı özelliği'
        verbose_name_plural = 'Hizmet fiyatı özellikleri'

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


class SocialAccounts(SingletonModel):
    instagram = models.URLField('Link')
    facebook = models.URLField('Link')
    pinterest = models.URLField('Link')

    class Meta:
        verbose_name = 'Sosyal medya hesapları'
        verbose_name_plural = 'Sosyal medya hesapları'


class DoctorInfo(SingletonModel):
    full_name = models.CharField('Adı soyadı', max_length=128)
    area = models.CharField('Uzmanlık alanı', max_length=128)
    paragraph = models.TextField('Kısa paragraf')

    class Meta:
        verbose_name = 'Doktor bilgileri'
        verbose_name_plural = 'Doktor bilgileri'
