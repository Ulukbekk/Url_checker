from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

BROKER_URL = 'redis://localhost:6379'
app = Celery('core', broker=BROKER_URL)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'add-every-1-hour': {
        'task': 'urls.tasks.chek_url',
        'schedule': crontab(hour='*/1')
    },
}

app.autodiscover_tasks()