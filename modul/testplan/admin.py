from django.contrib import admin

from .models import TestPlan, LogPlan, PlanCase

admin.site.register(TestPlan)
admin.site.register(LogPlan)
admin.site.register(PlanCase)
# Register your models here.
