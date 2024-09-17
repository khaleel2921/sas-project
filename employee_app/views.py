from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from  django.http import  HttpResponse
from . models import employee
from . forms import employeeForm
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'index.html')
def add_employee(request):
    if request.method=="POST":
        employeeid=request.POST['employeeid']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        contactnumber=request.POST['contactnumber']
        department=request.POST['department']
        designation=request.POST['designation']
        user= employee(employeeid=employeeid,firstname=firstname,lastname=lastname,email=email,contactnumber=contactnumber,department=department,designation=designation)
        user.save()
        return HttpResponse('Employee Id created')
    else:
        return render(request,'add_employee.html')

def employee_list(request):
    object=employee.objects.all()
    return render(request,"employee_list.html",{'list':object})

def searching(request):
    search=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        search=employee.objects.all().filter(Q(employeeid__contains=query)|Q(firstname__contains=query)|Q(department__contains=query))
    return render(request,'search.html',{'qr':query,'sr':search})
