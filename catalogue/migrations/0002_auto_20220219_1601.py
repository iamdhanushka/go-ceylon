# Generated by Django 3.2.12 on 2022-02-19 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='images',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='mainimage',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
