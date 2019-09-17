from django.db import models

# Create your models here.

class Word(models.Model):
	Korean = models.CharField(max_length=10)
	English = models.CharField(max_length=20)
	Uzb = models.CharField(max_length=20)
	Russian = models.CharField(max_length=20)
	
	def __str__(self):
		return self.Korean