from __future__ import unicode_literals
from django.db import models

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    department = models.CharField(max_length=20)

    def __str__(self):
        return self.name
