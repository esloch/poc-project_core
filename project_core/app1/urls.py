from django.urls import path
from .views import submit_metadata, success_view

urlpatterns = [
    path('submit_metadata/', submit_metadata, name='submit_metadata'),
    path('success/', success_view, name='success_url'),
]
