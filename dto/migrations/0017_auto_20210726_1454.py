# Generated by Django 3.2.5 on 2021-07-26 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dto', '0016_auto_20210726_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='four',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='nongear',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='two',
            name='date',
            field=models.DateField(),
        ),
    ]
