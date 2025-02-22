# Generated by Django 5.1.5 on 2025-01-29 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_contactinfo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactinfo',
            options={'verbose_name': 'İletişim bilgileri', 'verbose_name_plural': 'İletişim bilgileri'},
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='address_gm_src',
            field=models.URLField(default='', verbose_name='Google harita iframe linki'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='phone_number_repr',
            field=models.CharField(max_length=128, verbose_name='Telefon numarası (metin)'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='phone_number_wa_repr',
            field=models.CharField(max_length=128, verbose_name='Whatsapp numarası (metin)'),
        ),
    ]
