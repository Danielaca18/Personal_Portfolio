from django.db import models

from projects.models import Project

class Job(models.Model):
    """Model definition for job."""
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    summary = models.CharField(max_length=400)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class School(models.Model):
    """Model definition for school."""
    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    graduation_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Skill(models.Model):
    """Model definition for skill."""
    name = models.CharField(max_length=100)
    summary = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Person(models.Model):
    """Model definition for person."""
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    site = models.CharField(max_length=100, null=True, blank=True)
    objective = models.CharField(max_length=600)
    image = models.CharField(max_length=100, blank=True)
    projects = models.ManyToManyField(Project, blank=True)
    jobs = models.ManyToManyField(Job, blank=True)
    schools = models.ManyToManyField(School, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)


    def __str__(self):
        return self.name
