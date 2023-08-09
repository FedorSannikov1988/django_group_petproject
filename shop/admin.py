from django.contrib import admin
from shop.models import SoftwareCategory, Software, FeaturesSoftware, DevelopmentTeam, FAQ, UsersQuestions, Cart


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ["question"]
    search_fields = ["question"]
    ordering = ["question"]


@admin.register(UsersQuestions)
class UsersQuestionsAdmin(admin.ModelAdmin):
    list_display = ["user", "question_timestamp"]
    fields = [("user", "question_timestamp"), "userquestion", "upload"]
    readonly_fields = ["user", "userquestion", "question_timestamp", "upload"]
    ordering = ["user", "question_timestamp"]


@admin.register(SoftwareCategory)
class SoftwareCategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    ordering = ["name"]


@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "quantity", "price"]
    fields = [("name", "category"), ("price", "quantity"), "image"]
    search_fields = ["name", "category"]
    ordering = ["name", "category", "quantity", "price"]


@admin.register(FeaturesSoftware)
class FeaturesSoftwareAdmin(admin.ModelAdmin):
    list_display = ["software"]
    readonly_fields = ["software"]
    ordering = ["software"]


@admin.register(DevelopmentTeam)
class DevelopmentTeamAdmin(admin.ModelAdmin):
    list_display = ["firstname", "lastname", "patronymic"]
    fields = [("firstname", "lastname", "patronymic"), ("telephone", "mail"), "role", "description_work", "image"]
    search_fields = ["firstname", "lastname", "patronymic"]
    ordering = ["firstname", "lastname", "patronymic"]


class CartAdmin(admin.TabularInline):
    model = Cart
    fields = ["software", "quantity", "created_timestamp"]
    readonly_fields = ["created_timestamp"]
    extra = 0