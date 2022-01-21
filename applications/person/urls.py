from django.urls import path
from . import views


app_name = "person_app"

urlpatterns = [
    path('person/list', views.PersonListView.as_view(), name='list'),
    path('person/search', views.PersonSearchView.as_view(), name='api_search'),
]
