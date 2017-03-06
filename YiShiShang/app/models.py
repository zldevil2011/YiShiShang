from django.db import models


class Data(models.Model):
	height = models.FloatField(default=0.0)
	weight = models.FloatField(default=0.0)
	bust = models.FloatField(default=0.0)
	waist_circumference = models.FloatField(default=0.0)
	hip_circumference = models.FloatField(default=0.0)
	collect_time = models.DateTimeField(null=True)

	def __unicode__(self):
		return str(self.pk)

# Create your models here.
