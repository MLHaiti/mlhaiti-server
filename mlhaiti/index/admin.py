from django.contrib import admin
from .models import Profile, Photo


admin.site.register(Profile)
admin.site.register(Photo)

admin.site.site_header = "ML Haiti Server"