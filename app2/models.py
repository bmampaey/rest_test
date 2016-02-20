from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Record(models.Model):
	name = models.TextField(null=True, blank=True)
