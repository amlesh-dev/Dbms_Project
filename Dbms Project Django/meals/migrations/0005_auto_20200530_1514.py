# Generated by Django 3.0.5 on 2020-05-30 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0004_meals_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
