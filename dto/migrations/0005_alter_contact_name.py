# Generated by Django 3.2.5 on 2021-07-15 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dto', '0004_auto_20210715_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]