from django.contrib import admin

# Register your models here.
from connections.persons.models import Contact, Person

admin.site.register(Contact)
admin.site.register(Person)
