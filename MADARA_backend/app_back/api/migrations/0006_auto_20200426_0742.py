# Generated by Django 2.2 on 2020-04-26 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_new'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='new',
            options={'verbose_name_plural': 'news'},
        ),
    ]