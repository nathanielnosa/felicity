# Generated by Django 5.0.1 on 2024-01-26 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0003_agent_is_agent_agent_is_approved_agent_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='is_mvp',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]