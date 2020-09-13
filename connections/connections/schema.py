import graphene
from graphene_django import DjangoObjectType

from connections.persons.models import Contact, Person

class ContactType(DjangoObjectType):
	class Meta:
		model = Contact
		fields = ("id", "mobileNumber", "emailId", "persons")

class PersonType(DjangoObjectType):
	class Meta:
		model = Person
		fields = ("id", "name", "contact")

class Query(graphene.ObjectType):
	all_persons = graphene.List(PersonType)
	contact_by_mobile_number = graphene.Field(ContactType, mobileNumber=graphene.String(required=True))

	def resolve_all_persons(root, info):
		return Person.objects.select_related("contact").all()
	
	def resolve_contact_by_mobile_number(root, info, mobileNumber):
		try:
			return Contact.objects.get(mobileNumber=mobileNumber)
		except Contact.DoesNotExist:
			return None

schema = graphene.Schema(query=Query)
