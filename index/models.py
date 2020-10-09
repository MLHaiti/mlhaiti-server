from django.db import models
from django.contrib.auth.models import User 
from django.utils.translation import ugettext_lazy as _

class Profile(models.Model):
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	code = models.CharField(max_length=45, unique=True)
	slug = models.SlugField(max_length=80, unique=True)

	MALE,FEMALE = 'M','F'
	GENDER = [(MALE,_('Male')),(FEMALE,_('Female'))]
	gender = models.CharField(max_length=2,blank=True,choices=GENDER)

	area_code = models.CharField(max_length=7,blank=True)
	phone = models.CharField(max_length=22,blank=True)

	verified = models.BooleanField(default=False)
	date_verified = models.DateTimeField(null=True,blank=True)

	@property 
	def full_name(self):
		if self.first_name or self.last_name:
			return "%s %s" % (self.first_name,self.last_name)
		return ""