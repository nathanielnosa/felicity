# Generated by Django 5.0.1 on 2024-01-23 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_alter_listing_listing_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_id',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]