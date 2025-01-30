# Generated by Django 5.1.5 on 2025-01-30 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_servicecategory_title_en_servicecategory_title_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='answer_en',
            field=models.TextField(null=True, verbose_name='Cevap'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_ru',
            field=models.TextField(null=True, verbose_name='Cevap'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_tr',
            field=models.TextField(null=True, verbose_name='Cevap'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_en',
            field=models.TextField(null=True, verbose_name='Soru'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ru',
            field=models.TextField(null=True, verbose_name='Soru'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_tr',
            field=models.TextField(null=True, verbose_name='Soru'),
        ),
    ]
