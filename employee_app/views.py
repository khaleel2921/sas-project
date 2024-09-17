from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from . models import employee
from . forms import employeeForm

# Create your views here.
def add_employee(request):
    if request.method=="POST":
        employeeid=request.POST['employeeid']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        contactnumber=request.POST['contactnumber']
        department=request.POST['department']
        designation=request.POST['designation']
        if employee.objects.filter(email=email).exists():
            return redirect('add_employee')
        else:
            user= employee.objects.create_user(employeeid=employeeid,firstname=firstname,lastname=lastname,email=email,contactnumber=contactnumber,department=department,designation=designation)
            user.save()
        print("Employee Id created")
    else:
        return render(request,'add_employee.html')
