from django import forms
from DanielApp.models import Student
from DanielApp.models import Event
from DanielApp.models import Post


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'age', 'phone_number']


class EmployeeForm(forms.Form):
    firstname = forms.CharField(label="Enter Firstname", max_length=100)
    lastname = forms.CharField(label="Enter Lastname", max_length=100)
    age = forms.IntegerField(label="Enter age")
    phoneNumber = forms.IntegerField(label="Enter phoneNumber")


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['VenueName', 'Address', 'ZipCode', 'ContactPhone', 'WebAddress', 'EmailAddress']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Author', 'Title', 'Text', 'Createddate', 'Publisheddate']
