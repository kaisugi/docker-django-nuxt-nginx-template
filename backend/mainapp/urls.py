from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('hello/', views.hello, name='hello')
]
