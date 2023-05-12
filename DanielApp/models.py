from django.db import models


# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    phone_number = models.IntegerField(null=True)

    class Meta:
        db_table = "Student"

    def __str__(self):
        return self.firstname + '' + self.lastname


class Employee(models.Model):
    Name = models.CharField(max_length=50)
    Position = models.CharField(max_length=50)
    Office = models.CharField(max_length=50)
    Age = models.IntegerField()
    StartDate = models.DateField()
    Salary = models.IntegerField()

    def __str__(self):
        return self.Name + '' + self.Position


class Event(models.Model):
    VenueName = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    ZipCode = models.IntegerField()
    ContactPhone = models.IntegerField()
    WebAddress = models.CharField(max_length=50)
    EmailAddress = models.CharField(max_length=50)

    def __str__(self):
        return self.VenueName + '' + self.Address


class Post(models.Model):
    Author = models.CharField(max_length=50)
    Title = models.CharField(max_length=50)
    Text = models.CharField(max_length=50)
    Createddate = models.DateTimeField(null=True)
    Publisheddate = models.DateTimeField(null=True)

    def __str__(self):
        return self.Author + '' + self.Title
