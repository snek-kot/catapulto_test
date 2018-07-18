from django.contrib import admin

from .models import TestCase, Step, LogCase

admin.site.register(TestCase)
admin.site.register(Step)
admin.site.register(LogCase)
# Register your models here.
