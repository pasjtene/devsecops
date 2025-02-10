from django import forms
from .models import Asset, AssetCategory, ComplianceStatus
from django.contrib.auth.models import User

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['name', 'price', 'quantity', 'description', 'category', 'risk_status', 'impact_level']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'reviewed_by': forms.Select(attrs={'class': 'form-control'}),
        }

class ComplianceStatusForm(forms.ModelForm):
    class Meta:
        model = ComplianceStatus
        fields = [
            'description', 'asset', 'framework', 'requirement', 'details', 'implementation_percent', 'completion_Status',
            'implementation_start_date','expected_completion_date','actual_implementation_date','owner','assigned_to','created_by'
            ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'reviewed_by': forms.Select(attrs={'class': 'form-control'}),
        }

