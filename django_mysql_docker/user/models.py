from django.db import models

class User(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    description = models.TextField()
    birth_date = models.DateTimeField()
