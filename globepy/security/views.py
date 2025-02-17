from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Asset, RegulatoryFramework, ComplianceStatus
from .forms import ComplianceStatusForm
from django.contrib.auth.models import User
from django.utils import timezone

