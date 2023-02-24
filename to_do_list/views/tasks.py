from django.shortcuts import render, redirect, get_object_or_404
from to_do_list.forms import TaskForm
from to_do_list.models import Task, StatusChoice


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "task.html", context={"task": task, "choices": StatusChoice.choices})


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("task_detail", pk=task.pk)
    else:
        form = TaskForm()

    return render(
        request,
        "task_create.html",
        context={"form": form, "choices": StatusChoice.choices},
    )


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            task.save()
            return redirect("task_detail", pk=task.pk)
    else:
        form = TaskForm(instance=task)

    return render(request, "task_update.html", context={"form": form, "task": task})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "task_confirm_delete.html", context={"task": task})


def task_confirm_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("index")


def tasks_delete(request):
    tasks = Task.objects.filter(is_deleted=False)
    if request.method == "POST":
        for task in tasks:
            x = request.POST.get(str(task.pk))
            print(x)
            if str(x) == "on":
                b = Task.objects.get(pk=task.pk)
                b.delete()
        return redirect("index")

    context = {"tasks": tasks, "choices": StatusChoice.choices}
    return render(request, "tasks_delete.html", context=context)
