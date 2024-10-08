# Generated by Django 5.1 on 2024-08-24 08:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=4000, null=True)),
                ('script', models.TextField(blank=True, max_length=4000, null=True)),
                ('access_groups', models.ManyToManyField(related_name='commands', to='auth.group')),
                ('access_users', models.ManyToManyField(related_name='commands', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
