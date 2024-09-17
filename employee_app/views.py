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
        return redirect('/')
    else:
        return render(request,'add_employee.html')


def employee_list(request):
    search_id = request.GET.get('search_id', None)
    if search_id:
        employees = employee.objects.filter(employeeid=search_id)
    else:
        employees = employee.objects.all()

    return render(request, "employee_list.html", {'list': employees})



