from django.db import models

class Admin_blog(models.Model):
	title = models.CharField(max_length=100)
	paragraph = models.TextField(max_length=None)
	image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
	date = models.DateField(auto_now_add=True)
	def __str__(self):
		return self.title

class Nueva_seccion(models.Model):
	name_section = models.CharField(max_length=100)
	def __str__(self):
		return self.name_section