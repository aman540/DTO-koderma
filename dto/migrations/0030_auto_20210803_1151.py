# Generated by Django 3.2.5 on 2021-08-03 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dto', '0029_alter_grievance_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='notesfile',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
