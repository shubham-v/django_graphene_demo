from django.db import models

# Create your models here.

class Contact(models.Model):
    emailId = models.CharField(max_length=100)
    mobileNumber = models.CharField(max_length=100)

    def __str__(self):
        return self.emailId + ' '  + self.mobileNumber

class Person(models.Model):
    name = models.CharField(max_length=100)
    contact = models.ForeignKey(
        Contact, related_name="persons", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
