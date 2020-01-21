from __future__ import unicode_literals

from django.db import models

# Create your models here.

class mydb(models.Model):
    field = models.CharField(max_length=100, default='', null=False)
    type = models.CharField(max_length=50, default='', null=False)
    default = models.CharField(max_length=255, default='', null=False)
    value = models.CharField(max_length=255, default='', null=True)

    def __str__(self):
        return self.field
