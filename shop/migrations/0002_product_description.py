# Generated by Django 2.1.4 on 2018-12-09 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='Some description', max_length=1000, verbose_name='product description'),
        ),
    ]
