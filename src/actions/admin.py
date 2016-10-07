from django.contrib import admin

from .models import Repair


@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    pass
