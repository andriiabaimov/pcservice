from django.contrib import admin

from .models import Partner, Repair


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    pass


@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    pass
