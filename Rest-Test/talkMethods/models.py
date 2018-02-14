# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Talk(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=20)
    Speaker = models.CharField(max_length=20)
    Venue=models.CharField(max_length=20)
    Duration=models.IntegerField()
