from django.contrib import admin
from users.models import User
from shop.admin import CartAdmin


@admin.register(User)
class SoftwareCategoryAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "is_superuser", "is_staff", "date_joined"]
    search_fields = ["username", "first_name", "last_name"]
    ordering = ["username", "is_superuser", "is_staff", "date_joined"]
    inlines = [CartAdmin]