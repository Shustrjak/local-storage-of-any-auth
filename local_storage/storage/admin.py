from django.contrib import admin

# Register your models here.
from .models import Storage


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = "id", "place", "login", "two_auth"
    list_display_links = "id", "place"

