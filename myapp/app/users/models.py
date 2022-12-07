from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from PIL import Image
# Create your models here.

class CustomUser(AbstractUser):
	first_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150)
	def __str__(self):
		return self.username


class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	address = models.IntegerField()
	city = models.CharField(max_length=100)
	postal_code = models.IntegerField()
	date_of_birth = models.DateField(blank=True, null=True)
	photo = models.ImageField(upload_to='profile_pics/%Y/%m/%d', blank=True)


	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)

