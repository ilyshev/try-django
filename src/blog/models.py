from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length = 120) #max_length - required
	content = models.TextField()
	active = models.BooleanField(default=True)
