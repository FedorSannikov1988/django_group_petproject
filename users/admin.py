from django.contrib import admin
from users.models import User, EmailVerification
from shop.admin import CartAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "is_superuser", "is_staff", "date_joined"]
    search_fields = ["username", "first_name", "last_name"]
    ordering = ["username", "is_superuser", "is_staff", "date_joined"]
    inlines = [CartAdmin]


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ["code", "user", "expiration"]
    fields = ["code", "user", "created", "expiration"]
    readonly_fields = ["created"]
