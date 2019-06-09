from django.contrib import admin

from .models import Job
from .models import Technology

admin.site.register(Job)
admin.site.register(Technology)
