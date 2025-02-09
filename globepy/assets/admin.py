from django.contrib import admin
from .models import *

#admin.site.register(RegulatoryFramework)
admin.site.register(Vendor)
admin.site.register(Risk)
admin.site.register(SecurityRequirement)

class ComplianceStatus(admin.ModelAdmin):
    list_display = ('asset', 'framework', 'requirement', 'details','owner')
    list_filter = ('asset','framework',)
    search_fields = ('framework', 'requirement')
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the object is being created
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
    
   

#admin.site.register(Asset, AssetAdmin)
admin.register(ComplianceStatus)

# Register your models here.
