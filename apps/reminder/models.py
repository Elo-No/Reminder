

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from apps.core.models import BaseModel
from apps.reminder.enums import NotificationStatus, RepeatStatus

User = get_user_model()


class Reminder(BaseModel):
    user = models.ForeignKey(
        verbose_name=_('User'),
        to=User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=32,
    )
    description = models.TextField(
        verbose_name=_('Description '),
        max_length=64,
        null=True,
        blank=True
    )
    remind_at = models.DateTimeField(
        verbose_name=_('Reminde_at'),
    )
    repeat = models.IntegerField(
        verbose_name=_('How Repeat ?'), choices=RepeatStatus.choices, default=RepeatStatus.DONT_REPEAT
    )
    notification_status = models.IntegerField(
        verbose_name=_('Notification Status ?'), choices=NotificationStatus.choices, default=NotificationStatus.NONE)

    def __str__(self):
        return f'{self.title} - {self.user.username}'

    class Meta:
        verbose_name = _(' Reminder')
        verbose_name_plural = _(' Reminder')
