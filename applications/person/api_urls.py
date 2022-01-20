from django.urls import path
from . import api_views


app_name = "person_app_api"

urlpatterns = [
    path('api/v1/person/list', api_views.PersonListApiView.as_view(), name='api_list'),
]
