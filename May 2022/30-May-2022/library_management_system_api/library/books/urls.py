from django.urls import path
from . import views

urlpatterns=[
    path('', views.ListBook.as_view())
]