# myproject/celery.py

from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_core.settings')

app = Celery('project_core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Make sure the broker URL is correct
app.conf.broker_url = 'redis://redis:6379/0'

