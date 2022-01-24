from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView
from .models import Person, Reunion
from .serializers import PersonSerializer, ReunionSerializer


class PersonListApiView(ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()


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


class ReunionListApiView(ListAPIView):
    serializer_class = ReunionSerializer
    queryset = Reunion.objects.all()
