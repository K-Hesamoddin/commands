# Generated by Django 5.1 on 2024-08-24 09:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('commands', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='access_groups',
            field=models.ManyToManyField(blank=True, null=True, related_name='commands', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='command',
            name='access_users',
            field=models.ManyToManyField(blank=True, null=True, related_name='commands', to=settings.AUTH_USER_MODEL),
        ),
    ]
