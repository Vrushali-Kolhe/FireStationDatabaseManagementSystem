from django.db import models

# Create your models here.
class Designation(models.Model):
    id=models.AutoField(primary_key=True)
    type=models.CharField(max_length=50)
    objects = models.Manager()

class Station(models.Model):
    id=models.AutoField(primary_key=True)
    contact=models.IntegerField()
    address=models.CharField(max_length=200)
    objects = models.Manager()

class Vehicle_type(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    mobile=models.IntegerField()
    water_capacity=models.IntegerField()
    objects = models.Manager()

class Vehicle(models.Model):
    id=models.AutoField(primary_key=True)
    vehicle_number=models.CharField(max_length=100)
    purchase_date=models.DateTimeField()
    status=models.CharField(max_length=100)
    vehicle_type_id = models.ForeignKey(Vehicle_type, on_delete= models.CASCADE,default="")
    station_id = models.ForeignKey(Station, on_delete=models.CASCADE,default="")
    objects = models.Manager()

class Staff(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=25)
    dob=models.DateField()
    contact=models.IntegerField()
    doj=models.DateField()
    salary=models.IntegerField()
    station_id=models.ForeignKey(Station, on_delete=models.CASCADE,default="")
    designation_id = models.ForeignKey(Designation, on_delete=models.CASCADE,default="")
    objects = models.Manager()

class Reporter(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    contact = models.IntegerField()
    reporting_date = models.DateField(default="")
    objects=models.Manager()

class Complaint(models.Model):
    id=models.AutoField(primary_key=True)
    description=models.CharField(max_length=2000)
    pin=models.IntegerField()
    street=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    objects = models.Manager()

class Act(models.Model):
    id=models.AutoField(primary_key=True)
    status=models.CharField(max_length=100)
    leaving_time=models.DateTimeField(auto_now_add=True)
    reaching_time=models.DateTimeField(auto_now_add=True)
    description=models.CharField(max_length=2000)
    objects = models.Manager()


