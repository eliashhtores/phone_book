from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView
from .serializers import PersonSerializer, ReunionSerializer, ReunionLinkedSerializer, PersonPaginatedSerializer, ReunionByPersonJobSerializer
from .models import Person, Reunion


class PersonListApiView(ListAPIView):
    serializer_class = PersonSerializer
    pagination_class = PersonPaginatedSerializer

    def get_queryset(self):
        return Person.objects.all().order_by('id')


class PersonSearchApiView(ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name is not None:
            return Person.objects.filter(name__icontains=name)
        return Person.objects.all()


class PersonCreateApiView(CreateAPIView):
    serializer_class = PersonSerializer


class PersonRetrieveApiView(RetrieveAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonDestroyApiView(DestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonUpdateApiView(RetrieveUpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class ReunionListApiView(ListAPIView):
    serializer_class = ReunionSerializer
    queryset = Reunion.objects.all()


class ReunionLinkedApiView(ListAPIView):
    serializer_class = ReunionLinkedSerializer
    queryset = Reunion.objects.all()


class ReunionByPersonJob(ListAPIView):
    serializer_class = ReunionByPersonJobSerializer

    def get_queryset(self):
        return Reunion.objects.get_reunion_job()
