from django.db import models
from django.contrib.auth.models import User

from common.utils import create_code, create_slug

class Forum(models.Model):
	class Meta:
		db_table = 'forums'

	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	code = models.CharField(max_length=60, unique=True)
	slug = models.SlugField(max_length=100, unique=True)

	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	subject = models.CharField(max_length=200)
	description = models.TextField(max_length=500, blank=True)

	messages = models.ManyToManyField('Message', blank=True, through='ForumMessage')

	def __str__(self):
		return self.subject

	def save(self, *args, **kwargs):
		if self.pk is None:
			self.code = create_code(self, 50)	
			self.slug = create_slug(self, field_name='subject')
		super(Forum, self).save(*args, **kwargs)

class Message(models.Model):
	class Meta:
		db_table = 'messages'

	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	created_by = models.ForeignKey(User, on_delete=models.CASCADE)	
	is_deleted = models.BooleanField(default=False) # Delete for everyone
	content = models.TextField(max_length=4000)
	black_list_users = models.ManyToManyField(User, blank=True, related_name='hiddenmessage_set',
						through='MessageUser', through_fields=('message', 'user'))

	def __str__(self):
		return self.content[:150]

## Intermediary Models
class MessageUser(models.Model):
	class Meta:
		db_table = 'message_jn_user'
		verbose_name = 'Hidden Message'

	message = models.ForeignKey('Message', on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)	
	date_hidden = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "%s hidden to %s" % (self.message.content[:50], self.user.username)

class ForumMessage(models.Model):
	class Meta:
		db_table = 'forum_jn_message'

	forum = models.ForeignKey('Forum', on_delete=models.CASCADE)
	message = models.ForeignKey('Message', on_delete=models.CASCADE)



