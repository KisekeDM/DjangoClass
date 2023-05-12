from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello, name='hello'),
    path('name/', views.name, name='name'),
    path('number/', views.evenodd, name='even'),
    path('index/', views.index, name='index'),
    path('table/', views.tables, name='table'),
    path('employee/', views.employee, name='employee'),
    path('vary/', views.variables, name='vary'),
    path('assignment/', views.emp, name='ass'),
    path('images/', views.images, name='img'),
    path('members/', views.members),
    path('student/', views.student),
    path('employeeform/', views.employeeform),
    path('session/', views.setsession),
    path('gsession/', views.getsession),
    path('form/', views.form),
    path('power/', views.power),
    path('event/', views.events),


]

