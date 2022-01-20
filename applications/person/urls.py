from django.urls import path
from . import views


app_name = "person_app"

urlpatterns = [
    path('person/list', views.PersonListView.as_view(), name='list'),
]
