from django.contrib import admin

from shop.models import SoftwareCategory, Software, FeaturesSoftware

from shop.models import DevelopmentTeam

admin.site.register(Software)
admin.site.register(SoftwareCategory)
admin.site.register(FeaturesSoftware)

admin.site.register(DevelopmentTeam)