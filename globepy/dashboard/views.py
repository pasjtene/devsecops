from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from assets.models import Asset

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
    #return render(request, "assets/assets_dashboard.html", {"vars": response_data, "name":"Pascal JT"})

def say_hello3(request):
    return JsonResponse({"response":"Hello world json"})

def say_hello4(request):
    response_data = {}
    response_data["erro"] = "No error found"
    response_data["message"] = "Hello world"
    return JsonResponse(response_data)