from django.contrib import admin
from shop.models import SoftwareCategory, Software, FeaturesSoftware, DevelopmentTeam, FAQ


admin.site.register(FAQ)
admin.site.register(Software)
admin.site.register(SoftwareCategory)
admin.site.register(FeaturesSoftware)
admin.site.register(DevelopmentTeam)
