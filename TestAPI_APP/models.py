from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Author(models.Model):
	user = models.OneToOneField(User,on_delete=CASCADE)
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Book(models.Model):
	author = models.ForeignKey(Author,on_delete = models.PROTECT)
	name = models.CharField(max_length=100)
	category = models.CharField(max_length=100)

	def __str__(self):
		return self.name