from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from to_do_list.models import Task, StatusChoice


def task_list(request: WSGIRequest):
    tasks = Task.objects.exclude(is_deleted=True)
    context = {"tasks": tasks, "choices": StatusChoice.choices}
    return render(request, "index.html", context=context)
