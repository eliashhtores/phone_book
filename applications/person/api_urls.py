from django.urls import path
from . import api_views


app_name = "person_app_api"

urlpatterns = [
    path('api/v1/person/list', api_views.PersonListApiView.as_view(), name='api_list'),
    path('api/v1/person/search',
         api_views.PersonSearchApiView.as_view(), name='api_search'),
    path('api/v1/person/create',
         api_views.PersonCreateApiView.as_view(), name='api_create'),
    path('api/v1/person/detail/<pk>',
         api_views.PersonRetrieveApiView.as_view(), name='api_detail'),
    path('api/v1/person/delete/<pk>',
         api_views.PersonDestroyApiView.as_view(), name='api_delete'),
    path('api/v1/person/update/<pk>',
         api_views.PersonUpdateApiView.as_view(), name='api_update'),
    path('api/v1/reunion/list', api_views.ReunionListApiView.as_view(),
         name='api_reunion_list'),
    path('api/v1/reunion/linked', api_views.ReunionLinkedApiView.as_view(),
         name='api_reunion_linked'),
    path('api/v1/reunion/by-person', api_views.ReunionByPersonJob.as_view(),
         name='api_reunion_by_person'),
]
