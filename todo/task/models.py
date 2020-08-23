from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.TextField()
 
    def __str__(self):
        return self.name