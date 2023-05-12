from django.contrib import admin
from DanielApp.models import Student
from DanielApp.models import Employee
from DanielApp.models import Event
from DanielApp.models import Post

# Register your models here.
admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(Event)
admin.site.register(Post)
