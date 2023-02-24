from django.urls import path
from to_do_list.views.base import task_list
from to_do_list.views.tasks import *

urlpatterns = [
    path("", task_list, name="index"),
    path("task/", task_list, name="index"),
    path("task/create", task_create, name="task_create"),
    path("task/<int:pk>", task_detail, name="task_detail"),
    path("task/<int:pk>/update/", task_update, name="task_update"),
    path("task/<int:pk>/delete/", task_delete, name="task_delete"),
    path("task/<int:pk>/confirm_delete/", task_confirm_delete, name="task_confirm_delete"),
    path("task/tasks_delete", tasks_delete, name="tasks_delete"),
]
