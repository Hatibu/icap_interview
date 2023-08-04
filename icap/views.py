from django.shortcuts import render, redirect
from .models import Asset

# Create your views here.

def index(request):
    asset= Asset.objects.all()
    return render(request, 'index.html',{'asset': asset})


# def add(request):
#     return render(request,'add.html')

# def addMember(request):
#     fname = request.POST['fname']
#     lname = request.POST['lname']
#     country = request.POST['country']
#     mem = Member(firstname=fname,lastname=lname, country=country)
#     mem.save()
#     return redirect('/')

# def delete(request,id):
#     mem = Member.objects.get(id=id)
#     mem.delete()
#     return redirect('/')