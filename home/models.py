from django.db import models

class Person(models.Model):
    """Model definition for person."""
    name = models.CharField(max_length=100)
    objective = models.CharField(max_length=600)
    image = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Job(models.Model):
    """Model definition for job."""
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    summary = models.CharField(max_length=400)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class School(models.Model):
    """Model definition for school."""
    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    
class Skill(models.Model):
    """Model definition for skill."""
    name = models.CharField(max_length=100)
    summary = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name