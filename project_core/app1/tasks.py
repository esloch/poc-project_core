from celery import shared_task
from .models import Metadata

@shared_task
def add_metadata(name: str):
    """Task to add metadata to the database."""
    metadata = Metadata.objects.create(name=name)
    return metadata.id
