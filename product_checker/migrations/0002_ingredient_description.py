# Generated by Django 3.2.20 on 2023-11-15 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_checker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
