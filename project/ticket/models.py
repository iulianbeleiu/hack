from django.db import models

# Create your models here.
class Ticket(models.Model):
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.name