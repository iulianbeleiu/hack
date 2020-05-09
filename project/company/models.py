from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=30, blank=False)
    address = models.TextField(blank=False)
    email = models.CharField(max_length=50, blank=False)
    phoneNumber = models.CharField(max_length=15, blank=False)
    fiscalData = models.TextField(blank=False)
    activityDomain = models.CharField(max_length=50, blank=False)
    revenueId = models.IntegerField()

    def __str__(self):  # __unicode__ for Python 2
        return "Name: {}, Adress: {}".format(self.name, self.address)