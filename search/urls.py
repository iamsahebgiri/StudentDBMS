from django.urls import path, include
from . import views

app_name = 'search'

urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.add, name="add"),
    path('view/<int:roll>', views.view, name="view")
]
