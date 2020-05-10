from django.db import models
from company.models import Job
from course.models import Course


class Unemployed(models.Model):
    class Meta:
        verbose_name_plural = "Unemployed"
    name = models.CharField(max_length=30, blank=False)
    dateOfBirth = models.DateField(null=True, blank=True, default='')
    address = models.TextField(blank=False)
    email = models.CharField(max_length=50, blank=False)
    phoneNumber = models.CharField(max_length=15, blank=False)
    cv = models.TextField(blank=True)
    itmDocuments = models.TextField(blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.name


class UnemployedJob(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    unemployed = models.ForeignKey(Unemployed, on_delete=models.CASCADE)


class UnemployedCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    unemployed = models.ForeignKey(Unemployed, on_delete=models.CASCADE)
    grade = models.IntegerField()
