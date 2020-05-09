from django.db import models


class Unemployed(models.Model):
    name = models.CharField(max_length=30, blank=False)
    dateOfBirth = models.DateField(null=True, blank=True, default='')
    address = models.TextField(blank=False)
    email = models.CharField(max_length=50, blank=False)
    phoneNumber = models.CharField(max_length=15, blank=False)
    cv = models.TextField(blank=True)
    itmDocuments = models.TextField(blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.name