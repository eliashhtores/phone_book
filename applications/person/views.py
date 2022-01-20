from django.views.generic import ListView
from .models import Person


class PersonListView(ListView):
    context_object_name = 'person_list'
    template_name = 'person/list.html'

    def get_queryset(self):
        return Person.objects.all()
