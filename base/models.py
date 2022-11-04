from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def user_directory_path(instance, filename):
	return 'images/{0}/'.format(filename)


class work(models.Model):
	name = models.CharField(max_length=500)
	types = models.CharField(max_length=400, null=True)
	acces = models.CharField(max_length=400, null=True)

class accept(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=500)
	types = models.CharField(max_length=400, null=True)
	acces = models.CharField(max_length=400, null=True)
	done = models.BooleanField(default=False)

class box(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	img = models.ImageField(upload_to=user_directory_path, null=True)
	name = models.CharField(max_length=500)
	types = models.CharField(max_length=400, null=True)
	acces = models.CharField(max_length=400, null=True)