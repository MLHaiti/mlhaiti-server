from django.db import models
from django.contrib.auth.models import User

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

	messages = models.ManyToManyField('ForumMessage', blank=True)

	def __str__(self):
		return self.subject

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

	message = models.ForeignKey('Message', on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)	
	date_hidden = models.DateTimeField(auto_now_add=True)

class ForumMessage(models.Model):
	class Meta:
		db_table = 'forum_jn_message'

	forums = models.ForeignKey('Forum', on_delete=models.CASCADE)
	message = models.ForeignKey('Message', on_delete=models.CASCADE)



