# Generated by Django 3.2.5 on 2021-07-16 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dto', '0009_four_nongear_two'),
    ]

    operations = [
        migrations.RenameField(
            model_name='four',
            old_name='adress',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='nongear',
            old_name='adress',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='two',
            old_name='adress',
            new_name='address',
        ),
    ]