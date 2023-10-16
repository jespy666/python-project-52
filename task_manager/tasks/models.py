from django.db import models
from task_manager.users.models import User
from task_manager.statuses.models import Status


class Task(models.Model):

    name = models.CharField(
        max_length=150,
        blank=False,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    creation_date = models.DateTimeField(
        auto_now_add=True
    )

    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='author'
    )

    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name='status'
    )

    task_performer = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='task_performer'
    )

    def __str__(self):
        return self.name
