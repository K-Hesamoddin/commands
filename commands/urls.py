from django.contrib import admin
from django.urls import path, include

from . import views
from django.views.generic import TemplateView

app_name = "commands"
urlpatterns = [
    path('run/<int:pk>', views.run_command, name='run'),
]