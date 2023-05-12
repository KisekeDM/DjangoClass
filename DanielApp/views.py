from django.shortcuts import render, redirect
from django.http import HttpResponse
from DanielApp.models import Student
from DanielApp.forms import StudentForm
from DanielApp.forms import EmployeeForm
from DanielApp.models import Event
from DanielApp.models import Post



# Create your views here.
def hello(request):
    return HttpResponse("Welcome to Django")


def name(request):
    return HttpResponse("Hello there Daniel")


def evenodd(request):
    x = 25
    if x % 2 == 0:
        return HttpResponse("Number is even")
    else:
        return HttpResponse("Number is odd")


def index(request):
    return render(request, 'index.html')


def tables(request):
    return render(request, 'Tables.html')


def employee(request):
    return render(request, 'Employee.html')


def variables(request):
    details = {
        "firstname": "Daniel",
        "lastname": "Mutunga",
        "age": 17,
        "place": "Westlands",
    }
    return render(request, 'Variables.html', details)


def emp(request):
    info = {
        "EmployeeName": "Daniel",
        "ID": "23435346543",
        "Salary": 170000,
    }
    return render(request, 'Emp.html', info)


def images(request):
    return render(request, 'Images.html')


def members(request):
    all = Student.objects.all().values()
    details = {
        "members": all
    }
    return render(request, 'Members.html', details)


def student(request):
    if request.method == 'post':
        form = StudentForm(request.post)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = StudentForm()
            return render(request, 'Student.html', {'form': form})


def employeeform(request):
    emp = EmployeeForm()
    return render(request, 'Employeeform.html', {'form': emp})


def setsession(request):
    request.session['firstname'] = 'Daniel'
    request.session['lastname'] = 'Mutunga'
    request.session['email'] = 'Daniel@gmail.com'
    return HttpResponse('Session has been successfully created')


def getsession(request):
    fname = request.session['firstname']
    lname = request.session['firstname']
    email = request.session['firstname']
    return HttpResponse(fname + ' ' + lname + ' ' + email)


def form(request):
    return render(request, 'Form.html')


def power(request):
    return render(request, 'Power.html')


def events(request):
    if request.method == 'post':
        form = Event(request.post)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = Event()
            return render(request, 'Eventform.html', {'form': form})

def post(request):
    if request.method == 'post':
        form = Post(request.post)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = Post()
            return render(request, 'Post.html', {'form': form})
