# Generated by Django 3.2.5 on 2021-07-26 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dto', '0021_auto_20210726_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='four',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='nongear',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='two',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
