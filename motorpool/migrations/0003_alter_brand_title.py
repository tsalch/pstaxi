# Generated by Django 3.2.9 on 2021-11-28 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorpool', '0002_alter_brand_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='title',
            field=models.CharField(max_length=104),
        ),
    ]
