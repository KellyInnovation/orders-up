from django.contrib import admin

from .models import Hostess

class HostessAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("party_name", "id",)}
