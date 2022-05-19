import random
import urllib.parse
import urllib.request

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.conf import settings
from django.urls import reverse

from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from tracker.models import User, Task
from tracker.forms import CreateTaskForm


def logout(request):
    token = request.session['AUTH_APP_TOKEN']
    data = {'token': token,
            'client_id': settings.AUTH_APP_ID,
            'client_secret': settings.AUTH_APP_SECRET}
    req = urllib.request.Request(
        'http://auth:8000/o/revoke_token/',
        method='POST',
        data=urllib.parse.urlencode(data).encode('ascii'),
        )
    resp = urllib.request.urlopen(req)
    return HttpResponseRedirect(reverse('tracker:index'))
    # request.session['AUTH_APP_TOKEN'] = ''
    # return redirect(settings.AUTH_APP_LOGIN_FORM_URL)

def index(request):
    user = request.user
    all_tasks = Task.objects.all()
    context = {'tasks': all_tasks}
    return render(request, 'index.html', context)

def my_tasks(request):
    user = request.user
    users_tasks = Task.objects.filter(assigned_on=user)
    context = {'tasks':  users_tasks}
    return render(request, 'tasks/tasks.html', context)

def create_task(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            # developers = User.objects.filter(role='developer')
            # all_users = User.objects.all()
            # random_user = random.randrange(0, len(all_users)) if len(all_users) > 0 else None
            assigned_on = form.cleaned_data['assigned_on']
            task = Task.objects.create(title=title, description=description, status='OP', assigned_on=assigned_on)#all_users[random_user])
            return HttpResponseRedirect(reverse('tracker:index'))
    else:
        form = CreateTaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        print(f'Task with pk {pk} DoesNotExist')
        return redirect(reverse('tracker:my_tasks'))
    return render(request, 'tasks/task_details.html', {'task': task})

def shuffle_tasks(request):
    if request.method == 'POST':
        developers = User.objects.filter(role='DEV')
        if developers:
            opened_tasks = Task.objects.filter(status='OP')
            for task in opened_tasks:
                task.assigned_on = developers[random.randrange(0, len(developers))]
                task.save()
        return redirect(reverse('tracker:index'))
    else:
        return JsonResponse({'response': 'Wrong method'})

def close_task(request, pk):
    if request.method == 'POST':
        try:
            task = Task.objects.get(pk=pk)
            task.status = 'DN'
            task.save()
            return render(request, 'tasks/task_details.html', {'task': task})
        except Task.DoesNotExist:
            print('aloha')
    return redirect(reverse('tracker:index'))
