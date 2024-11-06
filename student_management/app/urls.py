from django.urls import path
from . import views

urlpatterns=[
    path('home',views.home),
    path('edit/<id>',views.edit_std),
    path('delete/<id>',views.delete)
]