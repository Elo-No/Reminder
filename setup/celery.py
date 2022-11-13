from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from decouple import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')

app = Celery('setup')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'send_notification': {
        'task': 'apps.reminder.tasks.send_sms',
        'schedule': int(config('SCHEDULE')),
    },

}

app.autodiscover_tasks()