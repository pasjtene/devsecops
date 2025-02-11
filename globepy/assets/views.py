from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Asset, RegulatoryFramework, ComplianceStatus
from .forms import ComplianceStatusForm
from django.contrib.auth.models import User

# Create your views here.
def formeditors2(request):
    return HttpResponse('LMS --- Hello world...!!! <br/> Another hello world <br> link <a href="/lms/hello2">go to hello2 </a>')

@login_required
def formeditors(request):
    response_data = {}
    response_data["erro"] = "LMS -- No error found"
    response_data["message"] = "Hello world"
    return render(request, "dashboard/forms-editors.html", {"vars": response_data, "name":"Pascal JT"})

@login_required
def create_page(request):
    return render(request, "dashboard/create-page.html")

@login_required
def dashboardhome(request):
    response_data = {}
    response_data["erro"] = "LMS -- No error found"
    response_data["message"] = "Hello world"
    return render(request, "dashboard/index.html", {"vars": response_data, "name":"Pascal JT"})

def list_all_assets(request):
    assets = Asset.objects.all()
    total_price = sum(asset.price * asset.quantity for asset in assets) #cal culate the total price of all assets
    total_assets = sum(asset.quantity for asset in assets) # calculate the total number of assets
    total_unique_assets = assets.count()
    
    return render(request, 'assets/assets_dashboard.html', {
        'assets':assets,
        'total_price': round(total_price),
        'total_assets':total_assets,
        'total_unique_assets':total_unique_assets
        })

def update_compliance_requirement(request, id):
    #asset = Asset.objects.get(id=id)
    
    
    if request.method == 'POST':
        complianceItem = ComplianceStatus.objects.get(id=id)
        complianceItem.details = request.POST.get('details')
        complianceItem.description = request.POST.get('description')
        complianceItem.implementation_percent = request.POST.get('implementation_percent')
        
        
        category_id = request.POST.get('category')
        risk_status = request.POST.get('risk_status')
        risk_level = request.POST.get('risk_level')
        reviewed_by_id = request.POST.get('reviewed_by')

        #category = Category.objects.get(id=category_id)
        #reviewed_by = User.objects.get(id=reviewed_by_id) if reviewed_by_id else None

       # asset = Asset(
            
            #category=category,
            #risk_status=risk_status,
            #risk_level=risk_level,
            #created_by=request.user,
            #reviewed_by=reviewed_by,
        #)
        
        complianceItem.save()
    
    asset = Asset.objects.get(id=complianceItem.asset_id)
    users = User.objects.all()
    regulatoryFrameworks = RegulatoryFramework.objects.all()
    complianceItems = ComplianceStatus.objects.all()
    form = ComplianceStatusForm()
    completion_Status_choices = ComplianceStatus.COMPLETION_STATUS_CHOICES
    
    return render(request, 'assets/asset-details.html',{
        'asset':asset,
        'regulatoryFrameworks':regulatoryFrameworks,
        'complianceItems': complianceItems,
        'form': form,
        'users': users,
        'completion_status_choices':completion_Status_choices
    })
    
def assetdetails(request, id):
    asset = Asset.objects.get(id=id)
    users = User.objects.all()
    regulatoryFrameworks = RegulatoryFramework.objects.all()
    complianceItems = ComplianceStatus.objects.all()
    form = ComplianceStatusForm()
    completion_Status = ComplianceStatus.COMPLETION_STATUS_CHOICES
    
    return render(request, 'assets/asset-details.html',{
        'asset':asset,
        'regulatoryFrameworks':regulatoryFrameworks,
        'complianceItems': complianceItems,
        'form': form,
        'users': users,
        'completion_status_choices':completion_Status
    })