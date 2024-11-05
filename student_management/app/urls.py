from django.urls import path
from . import views

urlpatterns=[
    path('home',views.home),
    path('edit/<a>',views.edit_std),
    path('delete/<a>',views.delete)
]