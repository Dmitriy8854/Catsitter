# Generated by Django 2.2.19 on 2023-04-10 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catsitter_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='image',
            field=models.ImageField(blank=True, upload_to='catsitter_main/', verbose_name='Картинка'),
        ),
    ]
