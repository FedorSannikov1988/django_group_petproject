from django.contrib import admin

from shop.models import SoftwareCategory, SoftwareSubcategories, Software

admin.site.register(Software)
admin.site.register(SoftwareCategory)
admin.site.register(SoftwareSubcategories)