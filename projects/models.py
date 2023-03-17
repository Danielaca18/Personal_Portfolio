from django.db import models

class Project(models.Model):
    """Model definition for Project."""
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    image = models.FilePathField(path="projects/static/img")
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title