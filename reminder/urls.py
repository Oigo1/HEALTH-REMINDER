from django.urls import path
from .views import reminder_view

urlpatterns = [
    path('', reminder_view, name='reminder'),
]