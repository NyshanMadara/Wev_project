# Generated by Django 2.2 on 2020-04-25 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_product_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='like',
            field=models.IntegerField(default=1),
        ),
    ]
