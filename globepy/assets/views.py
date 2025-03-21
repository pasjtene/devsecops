from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Asset, RegulatoryFramework, RequirementAction
#from .forms import ComplianceStatusForm
from django.contrib.auth.models import User
from django.utils import timezone
from comments.models import Comment
from comments.forms import CommentForm
from datetime import datetime
from security.models import SecurityManagementRequirement
from security.models import ISMSFramework, Framework
import json
from pprint import pprint
from django.http import JsonResponse



# Create your views here.
def formeditors2(request):
    return HttpResponse('LMS --- Hello world...!!! <br/> Another hello world <br> link <a href="/lms/hello2">go to hello2 </a>')

def framework_requirements(request, assetid,frameworkid,frameworkname):
    # Fetch all requirements from the database
    #framework_data = ISMSFramework.objects.all()
    STATUS_CHOICES = [
        ('Complete', 'Complete'),
        ('InProgress', 'InProgress'),
        ('Canceled', 'Canceled'),
        ('Paused','Paused')
    ]
    
    framework_data = Framework.objects.get(id=frameworkid)
    framework_requirement_actions = RequirementAction.objects.filter(asset_id=assetid)
    #pprint(dir(framework_data))
    asset = Asset.objects.get(id=assetid)
    users = User.objects.all()
    comments = Comment.objects.filter(asset_id=asset.id, parent_comment__isnull=True)
    
    
    
    context = {
        #'framework_data': json.dumps(framework_data.requirements),
        'framework_requirements': framework_data.requirements['requirements'],
        'framework_name': frameworkname,
        'framework_description': framework_data.description,
        'framework_id': framework_data.id,
        'framework_recommendations': framework_data.recommendations,
        'asset': asset,
        'users': users,
        #'completion_Status_choices': completion_Status_choices,
        #'security_requirement_items': security_requirement_items,
        'comments': comments,
        #'complianceItems': complianceItems,
        'STATUS_CHOICES': STATUS_CHOICES,
        'framework_requirement_actions': framework_requirement_actions
    }
    return render(request, 'assets/framework_requirements.html', context)
    #return JsonResponse(framework_data.requirements['requirements'], safe=False)

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
def create_requirement_action(request,frameworkid, assetid, requirementid):
     
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
        
        framework_data = Framework.objects.get(id=frameworkid)
        
        requirement_action = RequirementAction (
            framework_id = frameworkid,
            framework_name = framework_data.framework_name,
            requirement_codename = "1_2",
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
        
        requirement_action.save()
     return redirect('asset-details',id=assetid)   
      
  
@login_required
def update_requirement_action(request, requirementitemid):
     
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
            
        requirement_item = RequirementAction.objects.filter(id=requirementitemid)
        
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
def assetdetails(request, id):
    asset = Asset.objects.get(id=id)
    users = User.objects.all()
    regulatoryFrameworks = RegulatoryFramework.objects.all()
    #complianceItems = ComplianceStatus.objects.all()
    #security_requirement_items = RequirementStatus.objects.filter(asset_id=id)
    framework_requirement_actions = RequirementAction.objects.filter(asset_id=id)
    #security_requirements =  SecurityManagementRequirement.objects.filter(parent_requirement__isnull=True).order_by('order').values()
    security_requirements =  SecurityManagementRequirement.objects.filter(parent_requirement__isnull=True)
    #form = ComplianceStatusForm()
    #completion_Status = ComplianceStatus.COMPLETION_STATUS_CHOICES
    now = timezone.now()
    comment_form = CommentForm()
    comments = Comment.objects.filter(asset_id=id, parent_comment__isnull=True).order_by('-created_date')  # Fetch top-level comments only
    STATUS_CHOICES = [
        ('Complete', 'Complete'),
        ('InProgress', 'InProgress'),
        ('Canceled', 'Canceled'),
        ('Paused','Paused')
    ]
    
    return render(request, 'assets/asset-details.html',{
        'asset':asset,
        'regulatoryFrameworks':regulatoryFrameworks,
        #'complianceItems': complianceItems,
        #'form': form,
        'users': users,
        'completion_status_choices':STATUS_CHOICES,
        'now':now,
        'comment_form':comment_form,
        'comments':comments,
        #'securityRequirementItems': security_requirement_items,
        'security_requirements': security_requirements,
        'framework_requirement_actions': framework_requirement_actions
        
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
def add_comment_json(request, assetid, parent_id=None):
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
            return JsonResponse({
                'success': True,
                'comment_text': comment.comment_text,
                'comment_id': comment.id,
                'parent_id': parent_id,
                'message':"commnent created successfully",
                'created_date': comment.created_date,
                'created_by': request.user.get_full_name()
                })
    else:
        comment_form = CommentForm()
        messages.error(request, "The form is not valid")
        
    return JsonResponse({'error': 'Invalid form data.'}, status=400)



@login_required
def delete_comment(request, comment_id):
    comment= get_object_or_404(Comment, id=comment_id)
    
    # check if the user is the creator of the comment or a super user
    if request.user == comment.created_by or request.user.is_superuser:
        comment.delete()
        
        return JsonResponse({'success': True,'comment_text': comment.comment_text, 'comment_id': comment_id, 'message':"commnent deleted successfully"})
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
        
        
        
    