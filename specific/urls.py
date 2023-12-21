from specific.views import *
from django.urls import path

app_name='Specific'
urlpatterns=[
    path('Myntra/',Myntra,name='Myntra'),
    path('Urbanic/',Urbanic,name='Urbanic'),
]