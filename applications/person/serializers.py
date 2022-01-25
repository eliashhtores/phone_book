from itertools import count
from rest_framework import serializers, pagination
from .models import Person, Reunion, Hobby


class HobbiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ('name',)


class PersonSerializer(serializers.ModelSerializer):
    hobbies = HobbiesSerializer(many=True)

    class Meta:
        model = Person
        fields = ('id', 'name', 'job_title', 'email', 'phone',
                  'country', 'photo', 'notes', 'hobbies')


class PersonPaginatedSerializer(pagination.PageNumberPagination):
    page_size = 10
    max_page_size = 100


class ReunionSerializer(serializers.ModelSerializer):
    person = PersonSerializer()
    date_time = serializers.SerializerMethodField()

    class Meta:
        model = Reunion
        fields = ('id', 'subject', 'date', 'time', 'person', 'date_time')

    def get_date_time(self, obj):
        return str(obj.date) + ' ' + str(obj.time)


class ReunionLinkedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reunion
        fields = ('id', 'subject', 'date', 'time', 'person')
        extra_kwargs = {
            'person': {'view_name': 'person_app_api:api_detail', 'lookup_field': 'pk'}
        }


class ReunionByPersonJobSerializer(serializers.Serializer):
    person__job_title = serializers.CharField()
    person__job_title__count = serializers.IntegerField()
