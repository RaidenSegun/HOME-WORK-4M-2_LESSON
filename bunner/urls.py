from django.urls import path
from bunner.views import bunner

urlpatterns = [
    path('', bunner, name='bunner'),
    path('list/', list, name='list')
]