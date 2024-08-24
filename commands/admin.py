from django.contrib import admin
from .models import Command

# Register your models here.


@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'run_link']
    filter_horizontal = ('access_users', 'access_groups')


# admin.site.register(Command)
