from django.contrib import admin
from .models import *
# Register your models here.


class Sensor_Admin(admin.ModelAdmin):
	list_display = ["time", "oximeter", "temp"]

class Patient_Admin(admin.ModelAdmin):
	list_display =[
	"first_name",
	"last_name",
	"DOB",
	"email",
	"mobile",
	"gender",
	"blood_group",
	"address",
	"pin_code",
	"state",
	"country",
	"weight",
	"height",
	"medical_history",
	"medical_problems",
	"allergies"]

class Care_Taker_Admin(admin.ModelAdmin):
	list_display =[
	"first_name",
	"last_name",
	"DOB",
	"email",
	"mobile",
	"gender",
	"address",
	"city",
	"pin_code",
	"state",
	"country"]

class Doctor_Admin(admin.ModelAdmin):
	list_display =[
	"name", 
	"age", 
	"email", 
	"experience",
	"designation",
	"mobile", 
	"hospital_name", 
	"hospital_address"
	]

admin.site.register(Care_Taker,Care_Taker_Admin)
admin.site.register(Sensor,Sensor_Admin)
admin.site.register(Patient,Patient_Admin)
admin.site.register(Doctor,Doctor_Admin)
		