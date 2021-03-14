from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=500)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name
