from django.db import models
from unemployed.models import Unemployed


class Skill(models.Model):
    name = models.CharField(max_length=30, blank=False)

    def __str__(self):  # __unicode__ for Python 2
        return self.name


class SkillMatrix(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    unemployed = models.ForeignKey(Unemployed, on_delete=models.CASCADE)
    grade = models.IntegerField()