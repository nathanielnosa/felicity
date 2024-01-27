# Generated by Django 5.0.1 on 2024-01-26 01:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0002_alter_agent_facebook_alter_agent_instagram_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='is_agent',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='is_approved',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='agent',
            name='photo_main',
            field=models.ImageField(blank=True, null=True, upload_to='agent/%Y%m%d/'),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('is_read', models.BooleanField(default=False, null=True)),
                ('subject', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('recipient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to='agents.agent')),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='agents.agent')),
            ],
            options={
                'ordering': ['is_read', '-created'],
            },
        ),
    ]
