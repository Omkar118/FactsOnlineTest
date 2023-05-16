from django.urls import path
from .views import language_version

urlpatterns = [
    path('api/version/', language_version, name='language_version'),
]
