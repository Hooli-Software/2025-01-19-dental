# Generated by Django 5.1.5 on 2025-01-30 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Başlık')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='base/gallery-image/image/', verbose_name='Resim')),
            ],
        ),
        migrations.DeleteModel(
            name='Advantage',
        ),
        migrations.DeleteModel(
            name='Portfolio',
        ),
    ]
