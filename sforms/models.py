from django.db import models

# Create your models here.
class Certificate(models.Model):
	name = models.CharField(max_length=256)
	pressure_formate = models.BooleanField(default=False)
	vernier_format = models.BooleanField(default=False)
	multimeter_format = models.BooleanField(default=False)

	def __str__(self):
		return self.name



