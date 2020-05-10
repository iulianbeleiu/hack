from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=30, blank=False)
    description = models.TextField(blank=False)

    def __str__(self):  # __unicode__ for Python 2
        return "Name: {}, Description: {}".format(self.name, self.description)
