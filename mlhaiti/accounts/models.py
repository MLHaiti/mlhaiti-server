from django.db import models
from django.contrib.auth.models import User 
from django.utils.translation import ugettext_lazy as _
from django.utils.deconstruct import deconstructible

from mlhaiti.common.utils import create_code, create_slug, NOW

class Profile(models.Model):
	MALE,FEMALE = 'M','F'
	GENDER = [(MALE,_('Male')),(FEMALE,_('Female'))]

	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	code = models.CharField(max_length=45, unique=True)
	slug = models.SlugField(max_length=80, unique=True)
	gender = models.CharField(max_length=2,blank=True,choices=GENDER)
	photo = models.OneToOneField("Photo", blank=True,null=True,on_delete=models.SET_NULL)
	area_code = models.CharField(max_length=7,blank=True)
	phone = models.CharField(max_length=22,blank=True)

	verified = models.BooleanField(default=False)
	date_verified = models.DateTimeField(null=True,blank=True)

	class Meta:
		db_table = 'profiles'

	def __str__(self):
		return self.full_name

	@property 
	def first_name(self):
		return self.user.first_name

	@property
	def last_name(self):
		return self.user.last_name

	@property 
	def full_name(self):
		if self.first_name or self.last_name:
			return "%s %s" % (self.first_name,self.last_name)
		return ""

	def save(self, *args, **kwargs):
		if self.pk is None:
			self.code = create_code(self, 40)	
			self.slug = create_slug(self, field_name='full_name')
		super(Profile, self).save(*args, **kwargs)

@deconstructible
class object_directory_path(object):
	def __init__(self, prefix):
		self.prefix = prefix

	def __call__(self, instance, filename):
		ext = filename.split('.')[-1]
		date = NOW().strftime("%Y-%m-%dT%H:%M:%S")
		if instance.pk:
			ID = instance.pk
		else:
			ID = instance.generer(4).upper()

		filename = "uploaded-photos/%s/IMG-%s-ID-%s.%s" % (self.prefix,date,ID, ext)
		return filename

class Photo(models.Model):
	class Meta:
		db_table = 'profile_photos'

	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	code = models.CharField(max_length=11)

	photo = models.ImageField(upload_to=object_directory_path('original_size'), blank=True)
	photo600 = models.ImageField(upload_to=object_directory_path('600x600'), blank=True)
	photo450 = models.ImageField(upload_to=object_directory_path('450x450'), blank=True)
	photo300 = models.ImageField(upload_to=object_directory_path('300x300'), blank=True)
	photo200 = models.ImageField(upload_to=object_directory_path('200x200'), blank=True)
	photo150 = models.ImageField(upload_to=object_directory_path('150x150'), blank=True)
	photo100 = models.ImageField(upload_to=object_directory_path('100x100'), blank=True)
	photo75 = models.ImageField(upload_to=object_directory_path('75x75'), blank=True)
	photo37 = models.ImageField(upload_to=object_directory_path('37x37'), blank=True)
	photo18 = models.ImageField(upload_to=object_directory_path('18x18'), blank=True)
