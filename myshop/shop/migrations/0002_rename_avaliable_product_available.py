# Generated by Django 4.2 on 2023-04-20 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='avaliable',
            new_name='available',
        ),
    ]
