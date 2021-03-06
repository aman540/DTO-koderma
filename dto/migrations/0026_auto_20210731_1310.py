# Generated by Django 3.2.5 on 2021-07-31 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dto', '0025_auto_20210728_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checknama',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('name', models.CharField(max_length=40, null=True)),
                ('regno', models.CharField(max_length=10, null=True)),
                ('vt', models.CharField(max_length=50, null=True)),
                ('chalanno', models.IntegerField()),
            ],
        ),
        migrations.AlterModelTable(
            name='four',
            table='dto_four',
        ),
        migrations.AlterModelTable(
            name='nongear',
            table='dto_nongear',
        ),
        migrations.AlterModelTable(
            name='two',
            table='dto_two',
        ),
    ]
