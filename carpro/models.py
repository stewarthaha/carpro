from django.db import models

class Summary(models.Model):
    car_number = models.CharField(max_length=1)
    issue_date = models.DateTimeField('date published')

