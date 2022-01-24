from django.contrib import admin
from .models import Person, Hobby, Reunion


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_title', 'country')
    list_filter = ('country',)
    search_fields = ('name', 'job_title', 'email', 'phone', 'country')


admin.site.register(Person, PersonAdmin)
admin.site.register(Hobby)
admin.site.register(Reunion)
