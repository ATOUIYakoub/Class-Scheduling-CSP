from django.urls import path
from .views import TimetableListCreate

urlpatterns = [
    path('', TimetableListCreate.as_view(), name='contact'),
]
