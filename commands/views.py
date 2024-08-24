import datetime
import subprocess

from django.contrib.admindocs.views import ModelDetailView
from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import render

from commands.models import Command


# Create your views here.


def run_command(request, pk, *args, **kwargs):
    if not request.user.has_perm('app_label.permission_code'):
        return HttpResponseForbidden("You don't have permission to access this page.")
    response = dict()
    command = Command.objects.filter(pk=pk)[0]
    if command:
        start_time = datetime.datetime.now()
        response['start at'] = datetime.datetime.strftime(start_time, '%Y-%m-%d')
        response['result'] = ""
        if request.user and request.user in command.access_users.all() or request.user.groups.all() & command.access_groups.all():
            response['title'] = command.title
            response['description'] = command.description
            response['script'] = command.script.replace('\r\n', ' && ')
            # for cmd in command.script.split('\r\n'):
            result = subprocess.run(response['script'], shell=True, capture_output=True, text=True)
            response['result'] += f'''run --> result ({'ERR' if result.returncode else 'OK'}): [{result.stderr if result.returncode else result.stdout}]-- run at: {datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d")}          '''
        else:
            response['result'] = 'You have not access to command!'
    else:
        response['result'] = 'Command not found!'

    return JsonResponse(response)