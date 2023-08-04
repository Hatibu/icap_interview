from django.shortcuts import render, redirect
from .models import Asset,User
from .forms import AssetForm

# Create your views here.
def getUser(request):
    users = User.objects.all()
    return render(request, 'add.html', {'users': users})

def index(request):
    asset= Asset.objects.all()
    return render(request, 'index.html',{'asset': asset})


def add(request):
    return render(request,'add.html')

def addAsset(request):
    if request.method == 'POST':
       
        user_name = request.POST['user']
        asset_name = request.POST['name']
        asset_type = request.POST['type']

        user, _ = User.objects.get_or_create(name=user_name)

        Asset.objects.create(user=user, name=asset_name, type=asset_type)

        # Redirect to a success page
        return redirect('/')

    return render(request, 'add.html')

def delete(request,id):
    mem = Asset.objects.get(id=id)
    mem.delete()
    return redirect('/')

def update(request,id):
    asset = Asset.objects.get(id=id)
    return render(request, 'update.html',{'asset': asset})

def uprec(request,id):
    name = request.POST['name']
    type = request.POST['type']
    asset = Asset.objects.get(id=id)
    asset.name = name
    asset.type = type
    asset.save()
    return redirect('/')
