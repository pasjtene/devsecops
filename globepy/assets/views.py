from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Asset, RegulatoryFramework, ComplianceStatus, RequirementStatus
from .forms import ComplianceStatusForm
from django.contrib.auth.models import User
from django.utils import timezone
from comments.models import Comment
from comments.forms import CommentForm
from datetime import datetime
from security.models import SecurityManagementRequirement
from security.models import ISMSFramework
import json


# Create your views here.
def formeditors2(request):
    return HttpResponse('LMS --- Hello world...!!! <br/> Another hello world <br> link <a href="/lms/hello2">go to hello2 </a>')

def iso27001_requirements(request, assetid):
    # Fetch all requirements from the database
    #framework_data = ISMSFramework.objects.all()
    framework_data = ISMSFramework.objects.get(id=1)
    asset = Asset.objects.get(id=assetid)
    context = {
        'framework_data': json.dumps(framework_data.requirements),
        'asset': asset
    }
    return render(request, 'assets/framework_requirements.html', context)

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

@login_required
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


@login_required
def create_compliance_requirement(request,frameworkid, assetid, requirementid):
     
     if request.method == 'POST':
        
        owner_id = request.POST.get('owner_id')
        
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
        
        
        compliance_status.save()
     return redirect('asset-details',id=assetid)
    

@login_required
def create_security_requirement(request,frameworkid, assetid, requirementid):
     
     if request.method == 'POST':
        
        owner_id = request.POST.get('owner_id')
        actual_implementation_date = request.POST.get('actual_implementation_date')
        expected_completion_date = request.POST.get('expected_completion_date')
        implementation_start_date = request.POST.get('implementation_start_date')
        
        # check if the user has suplied dates for the activity, otherwise, set date to now
        if len(actual_implementation_date) < 3:
            actual_implementation_date = timezone.now()
            #actual_implementation_date = datetime.strptime(actual_implementation_date, "%d/%b/%Y:%X %z").strftime("%Y-%m-%d %X")
        
        
        if len(expected_completion_date) < 3:
            expected_completion_date = timezone.now()
            
        
        if len(implementation_start_date) < 3:
            implementation_start_date = timezone.now()
        
        
        requirement_status = RequirementStatus (
            framework_id = frameworkid,
            asset_id = assetid,
            requirement_id = requirementid,
            details = request.POST.get('details'),
            description = request.POST.get('description'),
            implementation_percent = request.POST.get('implementation_percent'),
            completion_Status = request.POST.get('completion_status'),
            owner = User.objects.get(id=owner_id) if owner_id else None,
            actual_implementation_date = actual_implementation_date,
            expected_completion_date = expected_completion_date,
            implementation_start_date = implementation_start_date,
            assigned_to_id = request.POST.get('assigned_to_id'),
            
        )
        
        requirement_status.save()
     return redirect('asset-details',id=assetid)        
  
@login_required
def update_security_requirement(request, requirementitemid):
     
     if request.method == 'POST':
        
        owner_id = request.POST.get('owner_id')
        actual_implementation_date = request.POST.get('actual_implementation_date')
        expected_completion_date = request.POST.get('expected_completion_date')
        implementation_start_date = request.POST.get('implementation_start_date')
        
        # check if the user has suplied dates for the activity, otherwise, set date to now
        if len(actual_implementation_date) < 3:
            actual_implementation_date = timezone.now()
            #actual_implementation_date = datetime.strptime(actual_implementation_date, "%d/%b/%Y:%X %z").strftime("%Y-%m-%d %X")
        
        
        if len(expected_completion_date) < 3:
            expected_completion_date = timezone.now()

        if len(implementation_start_date) < 3:
            implementation_start_date = timezone.now()
            
        requirement_item = RequirementStatus.objects.filter(id=requirementitemid)
        
        requirement_item.update (
            details = request.POST.get('details'),
            description = request.POST.get('description'),
            implementation_percent = request.POST.get('implementation_percent'),
            completion_Status = request.POST.get('completion_status'),
            owner = User.objects.get(id=owner_id) if owner_id else None,
            actual_implementation_date = actual_implementation_date,
            expected_completion_date = expected_completion_date,
            implementation_start_date = implementation_start_date,
            assigned_to_id = request.POST.get('assigned_to_id'),
            
        )
        
        #requirement_status.save()
     return redirect('asset-details',id=requirement_item[0].asset_id)       
    

@login_required
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
        comment_form = CommentForm()
        
   
    asset = Asset.objects.get(id=complianceItem.asset_id)
    comments = Comment.objects.filter(asset_id=asset.id, parent_comment__isnull=True)  # Fetch top-level comments only
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
        'comment_form':comment_form,
        'comments':comments
    })

@login_required  
def assetdetails(request, id):
    asset = Asset.objects.get(id=id)
    users = User.objects.all()
    regulatoryFrameworks = RegulatoryFramework.objects.all()
    complianceItems = ComplianceStatus.objects.all()
    security_requirement_items = RequirementStatus.objects.filter(asset_id=id)
    #security_requirements =  SecurityManagementRequirement.objects.filter(parent_requirement__isnull=True).order_by('order').values()
    security_requirements =  SecurityManagementRequirement.objects.filter(parent_requirement__isnull=True)
    form = ComplianceStatusForm()
    completion_Status = ComplianceStatus.COMPLETION_STATUS_CHOICES
    now = timezone.now()
    comment_form = CommentForm()
    comments = Comment.objects.filter(asset_id=id, parent_comment__isnull=True)  # Fetch top-level comments only
    
    return render(request, 'assets/asset-details.html',{
        'asset':asset,
        'regulatoryFrameworks':regulatoryFrameworks,
        'complianceItems': complianceItems,
        'form': form,
        'users': users,
        'completion_status_choices':completion_Status,
        'now':now,
        'comment_form':comment_form,
        'comments':comments,
        'securityRequirementItems': security_requirement_items,
        'security_requirements': security_requirements
        
    })
 
@login_required    
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
        messages.error(request, "The form is not valid")
        
    return redirect('asset-details',id=assetid)
    

@login_required
def delete_comment(request, comment_id):
    comment= get_object_or_404(Comment, id=comment_id)
    
    # check if the user is the creator of the comment or a super user
    if request.user == comment.created_by or request.user.is_superuser:
        comment.delete()
        
        return JsonResponse({'success': True, 'comment_text': comment.comment_text, 'comment_id': comment_id, 'message':"commnent deleted successfully"})
    else:       
        return JsonResponse({'error': 'Invalid form data.'}, status=400)
    

@login_required
def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.created_by:
        return JsonResponse({'error': 'You do not have permission to update this comment.'}, status=403)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'comment_text': comment.comment_text, 'comment_id': comment.id,'message':"commnent updated successfully"})
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)
    else:
        form = CommentForm(instance=comment)
    return JsonResponse({'comment_text': comment.comment_text}) 
        
        
        
    