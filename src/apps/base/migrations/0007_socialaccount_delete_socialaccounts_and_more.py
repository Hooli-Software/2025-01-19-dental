# Generated by Django 5.1.5 on 2025-01-28 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_servicecategory_options_remove_service_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=128, verbose_name='Font awesome ikon kodu')),
                ('title', models.CharField(max_length=255, verbose_name='Başlık')),
                ('link', models.URLField(verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Sosyal medya hesabı',
                'verbose_name_plural': 'Sosyal medya hesapları',
            },
        ),
        migrations.DeleteModel(
            name='SocialAccounts',
        ),
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='base.servicecategory'),
        ),
    ]
