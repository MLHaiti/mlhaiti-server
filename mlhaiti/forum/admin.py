from django.contrib import admin
from .models import Forum, Message, ForumMessage, MessageUser

admin.site.register(Forum)
admin.site.register(Message)
admin.site.register(ForumMessage)
admin.site.register(MessageUser)

