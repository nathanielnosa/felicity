# Generated by Django 5.0.1 on 2024-01-23 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='facebook',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='instagram',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='linkedin',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='twitter',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
