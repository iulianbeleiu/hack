from django.db import models


class Revenue(models.Model):
    name = models.CharField(max_length=30, blank=True)
    intervalMin = models.IntegerField()
    intervalMax = models.IntegerField()
    percent = models.IntegerField()

    def __str__(self):  # __unicode__ for Python 2
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=30, blank=False)
    address = models.TextField(blank=False)
    email = models.CharField(max_length=50, blank=False)
    phoneNumber = models.CharField(max_length=15, blank=False)
    fiscalData = models.TextField(blank=False)
    activityDomain = models.CharField(max_length=50, blank=False)
    revenue = models.ForeignKey(Revenue, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.name


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=False)
    description = models.TextField(blank=False)
    price = models.IntegerField()

    def __str__(self):  # __unicode__ for Python 2
        return "Name: {}, Description: {}, Price: {}, Company: {}".format(self.name, self.description, self.price, self.company)


class Job(models.Model):
    name = models.CharField(max_length=30, blank=False)
    description = models.TextField(blank=False)
    availableFrom = models.DateField(blank=False)
    isActive = models.BooleanField(blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    creationDate = models.DateField(blank=False)

    def __str__(self):  # __unicode__ for Python 2
        return self.name