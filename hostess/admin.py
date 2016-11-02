from django.contrib import admin


class HostessAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("party_name", "id")}
