# -*- coding: UTF-8 -*-

from django.db import models

class proxy(models.Model):
	id = models.BigIntegerField(max_length=10)
	ip = models.CharField(max_length=20)
	post = models.BigIntegerField(max_length=10)
	status = models.BigIntegerField(max_length=2)