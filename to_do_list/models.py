from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


class StatusChoice(TextChoices):
    NEW = "NEW", "Новая"
    IN_PROCESS = "IN_PROCESS", "В процессе"
    DONE = "DONE", "Сделано"


class Task(models.Model):
    title = models.CharField(
        max_length=200, null=False, blank=False, verbose_name="Заголовок"
    )
    status = models.CharField(
        max_length=30,
        choices=StatusChoice.choices,
        verbose_name="Статус",
        default=StatusChoice.NEW,
    )
    date_to_do = models.CharField(
        max_length=10, null=False, blank=False, verbose_name="Дата выполнения"
    )
    description = models.TextField(
        max_length=200, null=False, blank=True, verbose_name="Описание"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата и время обновления"
    )
    is_deleted = models.BooleanField(verbose_name="Удалено", null=False, default=False)
    deleted_at = models.DateTimeField(
        verbose_name="Дата и время удаления", null=True, default=None
    )

    def __str__(self):
        return f"{self.description} - {self.date_to_do}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
