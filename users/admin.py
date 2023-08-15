from users.models import EmailVerification, \
                         PasswordRecovery, \
                         User
from shop.admin import CartAdmin
from django.contrib import admin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name",
                    "is_superuser", "is_staff", "date_joined"]
    search_fields = ["username", "first_name", "last_name"]
    ordering = ["username", "is_superuser", "is_staff",
                "date_joined"]
    inlines = [CartAdmin]


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ["code", "user", "expiration"]
    fields = ["code", "user", "created",
              "expiration"]
    readonly_fields = ["created"]


@admin.register(PasswordRecovery)
class PasswordRecoveryAdmin(admin.ModelAdmin):
    list_display = ["code", "user", "expiration",
                    "link_used"]
    fields = ["code", "user", "created",
              "expiration", "link_used"]
    readonly_fields = ["created"]
