from django.contrib.auth.models import User, Group
from django.db import models
from django.utils.safestring import mark_safe


button_style = "background-color: #04AA6D; border: none; color: white; padding: 5px 5px; text-align: center; text-decoration: none; display: inline-block; "
# Create your models here.


class Command(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=4000, blank=True, null=True)
    script = models.TextField(max_length=4000, blank=True, null=True)
    access_users = models.ManyToManyField(User,related_name='commands', blank=True, null=True)
    access_groups = models.ManyToManyField(Group,related_name='commands', blank=True, null=True)

    @property
    def run_link(self):
            return mark_safe(
                f'<button style="{button_style}" ><a target="blank" href="/commands/run/{self.id}">Run</a></button>')