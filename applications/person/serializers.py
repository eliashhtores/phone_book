from rest_framework import serializers
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


class ReunionSerializer(serializers.ModelSerializer):
    person = PersonSerializer()
    date_time = serializers.SerializerMethodField()

    class Meta:
        model = Reunion
        fields = ('id', 'subject', 'date', 'time', 'person', 'date_time')

    def get_date_time(self, obj):
        return str(obj.date) + ' ' + str(obj.time)
