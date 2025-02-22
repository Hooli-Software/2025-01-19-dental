# Generated by Django 5.1.5 on 2025-01-23 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_slide_type_alter_advantage_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='link',
        ),
        migrations.AddField(
            model_name='slide',
            name='button_link',
            field=models.URLField(blank=True, null=True, verbose_name='Link'),
        ),
        migrations.AddField(
            model_name='slide',
            name='button_text',
            field=models.CharField(blank=True, max_length=36, null=True, verbose_name='Buton metni'),
        ),
        migrations.AddField(
            model_name='slide',
            name='show_button',
            field=models.BooleanField(default=False, verbose_name='Buton gösterilsinmi?'),
        ),
        migrations.AddField(
            model_name='slide',
            name='subtitle',
            field=models.CharField(default='', max_length=128, verbose_name='Alt başlık'),
            preserve_default=False,
        ),
    ]
