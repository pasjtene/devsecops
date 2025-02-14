from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Asset, RegulatoryFramework, ComplianceStatus
from .forms import ComplianceStatusForm
from django.contrib.auth.models import User
from django.utils import timezone
from comments.models import Comment
from comments.forms import CommentForm

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

def create_compliance_requirement(request,frameworkid, assetid, requirementid):
     
     if request.method == 'POST':
        
        owner_id = request.POST.get('owner_id')
        #complianceItem.owner = User.objects.get(id=owner_id) if owner_id else None
        #complianceItem. actual_implementation_date = request.POST.get('actual_implementation_date')
        #complianceItem. expected_completion_date = request.POST.get('expected_completion_date')
        #complianceItem. implementation_start_date = request.POST.get('implementation_start_date')
        
        #assigned_to_id = request.POST.get('assigned_to_id')
        #complianceItem.assigned_to = User.objects.get(id=assigned_to_id) if assigned_to_id else None
        
        compliance_status = ComplianceStatus (
            framework_id = frameworkid,
            asset_id = assetid,
            requirement_id = requirementid,
            details = request.POST.get('details'),
            description = request.POST.get('description'),
            implementation_percent = request.POST.get('implementation_percent'),
            completion_Status = request.POST.get('completion_status'),
            owner = User.objects.get(id=owner_id) if owner_id else None,
            actual_implementation_date = request.POST.get('actual_implementation_date'),
            expected_completion_date = request.POST.get('expected_completion_date'),
            implementation_start_date = request.POST.get('implementation_start_date'),
            assigned_to_id = request.POST.get('assigned_to_id'),
            
        )
        

        #category = Category.objects.get(id=category_id)
        #reviewed_by = User.objects.get(id=reviewed_by_id) if reviewed_by_id else None
        
        compliance_status.save()
        asset = Asset.objects.get(id=assetid)
        users = User.objects.all()
        regulatoryFrameworks = RegulatoryFramework.objects.all()
        complianceItems = ComplianceStatus.objects.all()
        form = ComplianceStatusForm()
        completion_Status_choices = ComplianceStatus.COMPLETION_STATUS_CHOICES
        now = timezone.now()
    
        return render(request, 'assets/asset-details.html',{
        'asset':asset,
        'regulatoryFrameworks':regulatoryFrameworks,
        'complianceItems': complianceItems,
        'form': form,
        'users': users,
        'completion_status_choices':completion_Status_choices,
         'now':now,
    })
    
    
    
def update_compliance_requirement(request, id):
    #asset = Asset.objects.get(id=id)
    
    
    if request.method == 'POST':
        complianceItem = ComplianceStatus.objects.get(id=id)
        complianceItem.details = request.POST.get('details')
        complianceItem.description = request.POST.get('description')
        complianceItem.implementation_percent = request.POST.get('implementation_percent')
        complianceItem.completion_Status = request.POST.get('completion_status')
        owner_id = request.POST.get('owner_id')
        complianceItem.owner = User.objects.get(id=owner_id) if owner_id else None
        complianceItem. actual_implementation_date = request.POST.get('actual_implementation_date')
        complianceItem. expected_completion_date = request.POST.get('expected_completion_date')
        complianceItem. implementation_start_date = request.POST.get('implementation_start_date')
        
        assigned_to_id = request.POST.get('assigned_to_id')
        complianceItem.assigned_to = User.objects.get(id=assigned_to_id) if assigned_to_id else None
        
    
        
        complianceItem.save()
        now = timezone.now()
   
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
        'completion_status_choices':completion_Status_choices,
        'now':now,
    })
    
def assetdetails(request, id):
    asset = Asset.objects.get(id=id)
    users = User.objects.all()
    regulatoryFrameworks = RegulatoryFramework.objects.all()
    complianceItems = ComplianceStatus.objects.all()
    form = ComplianceStatusForm()
    completion_Status = ComplianceStatus.COMPLETION_STATUS_CHOICES
    now = timezone.now()
    comment_form = CommentForm()
    
    return render(request, 'assets/asset-details.html',{
        'asset':asset,
        'regulatoryFrameworks':regulatoryFrameworks,
        'complianceItems': complianceItems,
        'form': form,
        'users': users,
        'completion_status_choices':completion_Status,
        'now':now,
        'comment_form':comment_form
        
    })
    
def add_comment(request, assetid, parent_id=None):
    parent_comment = None
    asset = Asset.objects.get(id=assetid)
    
    if parent_id:
        parent_comment = get_object_or_404(Comment, id=parent_id)
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.created_by = request.user
            comment.parent_comment = parent_comment
            comment.asset = asset
            comment.save()
    else:
        comment_form = CommentForm()
        
    
    users = User.objects.all()
    regulatoryFrameworks = RegulatoryFramework.objects.all()
    complianceItems = ComplianceStatus.objects.all()
    form = ComplianceStatusForm()
    completion_Status = ComplianceStatus.COMPLETION_STATUS_CHOICES
    now = timezone.now()
    comments = Comment.objects.filter(asset_id=assetid, parent_comment__isnull=True)  # Fetch top-level comments only
    
    
    return render(request, 'assets/asset-details.html',{
        'asset':asset,
        'regulatoryFrameworks':regulatoryFrameworks,
        'complianceItems': complianceItems,
        'form': form,
        'users': users,
        'completion_status_choices':completion_Status,
        'now':now,
        'comment_form':comment_form,
        'parent_comment':parent_comment,
        'comments':comments
        
    })
        
    