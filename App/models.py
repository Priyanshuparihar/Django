from django.db import models
from django.utils import timezone

# Create your models here.

class Sensor(models.Model):
	time = models.DateTimeField(auto_now = True)
	spo2 = models.DecimalField(max_digits=20, decimal_places=5, default=0.00)
	bpm = models.DecimalField(max_digits=20, decimal_places=5, default=0.00)
	temp = models.DecimalField(max_digits=20, decimal_places=5, default=0.00)
	# temp = models.CharField(max_length=255,null=True)


class Patient(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	DOB = models.DateField()
	email = models.EmailField(max_length = 254)
	mobile = models.CharField(max_length=10)
	gender = models.CharField(max_length=10)
	blood_group = models.CharField(max_length=5)
	address = models.CharField(max_length=254)
	pin_code = models.IntegerField()
	state = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	weight = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
	height = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
	medical_history = models.CharField(max_length=254)
	medical_problems = models.CharField(max_length=254)
	allergies = models.CharField(max_length=254)

class Care_Taker(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	DOB = models.DateField()
	email = models.EmailField(max_length = 254)
	mobile = models.CharField(max_length=10)
	gender = models.CharField(max_length=10)
	address = models.CharField(max_length=254)
	city = models.CharField(max_length=50)
	pin_code = models.IntegerField()
	state = models.CharField(max_length=50)
	country = models.CharField(max_length=50)

class Doctor(models.Model):
	name = models.CharField(max_length=30)
	age = models.IntegerField()
	email =  models.EmailField(max_length = 254)
	experience = models.IntegerField()
	designation = models.CharField(max_length=30)
	mobile = models.CharField(max_length=10)
	hospital_name = models.CharField(max_length=50)
	hospital_address = models.CharField(max_length=254)

class Stream(models.Model):
	link = models.CharField(max_length=50)

class Medicine(models.Model):
	id = models.AutoField(primary_key=True)
	medicine_name = models.CharField(max_length=50)
	description = models.CharField(max_length=254)
	days = models.CharField(max_length=254)
	time =  models.TimeField()

class Audio(models.Model):
	time = models.DateTimeField(auto_now = True)
	record=models.FileField(upload_to= "audios/")


