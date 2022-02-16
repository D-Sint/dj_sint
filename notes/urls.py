from django.urls import path

from notes.views import *


urlpatterns = [
    path('', home, name='home'),
    path('notes/', notes, name='notes'),
]

