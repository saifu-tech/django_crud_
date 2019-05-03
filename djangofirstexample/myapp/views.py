from django.shortcuts import render,render_to_response,redirect
from myapp.forms import EmployeeForm
from myapp.models import Employee
# Create your views here.

def index(request):
	return render_to_response('index.html')

def about(request):
	return render_to_response('about.html')

def service(request):
	return render_to_response('service.html')

def add(request):
	return render(request, "add.html")

def savedata(request):
	request.POST
	employee = Employee(eid=request.POST['eid'],ename=request.POST['ename'],eemail=request.POST['eemail'],econtact=request.POST['econtact'])
	employee.save()
	return  redirect('/show')
def show(request):
	employees = Employee.objects.all()
	return render(request, "crudshow.html", {'employees':employees })

def edit(request, id):
	employee = Employee.objects.get(id = id)
	return render(request,"edit.html",{'employee':employee})

def update(request,id):
	employee = Employee.objects.get(id = id)
	employee.eid = request.POST['eid']
	employee.ename = request.POST['ename']
	employee.eemail = request.POST['eemail']
	employee.econtact = request.POST['econtact']
	employee.save()
	return redirect('/show')
	

def delete(request,id):
	employee = Employee.objects.get(id = id)
	employee.delete()
	return redirect("/show")