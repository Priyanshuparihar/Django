from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"])
def api_sensor(request):
	t = Sensor.objects.all()
	# data = "yes"
	data = {}
	j=0
	for i in t.iterator():
		data[j] = {
		            "Time" : i.time, 
		            "Oximeter" : i.oximeter, 
		            "Temperature" : i.temp
		           }
		j+=1
	return Response(data=data,status=status.HTTP_200_OK)

@api_view(["POST"])
def update_sensor(request):
	oximeter = request.data["oximeter"]
	print(oximeter)
	temp = request.data["temp"]
	print(temp)
	t = Sensor(oximeter=oximeter, temp=temp)
	t.save()
	return Response(data="Data Entry Succesful",status=status.HTTP_200_OK)


@api_view(["GET"])
def api_patient(request):
	obj_p = Patient.objects.all()
	data = {}
	j=0
	for i in obj_p.iterator():
		data[j] = {
					"first_name" : i.first_name,
		            "last_name": i.last_name,
					"DOB" : i.DOB,
					"email" : i.email,
					"mobile" : i.mobile,
					"gender" : i.gender,
					"blood_group" : i.blood_group,
					"address" :i.address,
					"pin_code" : i.pin_code,
					"state" : i.state,
					"country" : i.country,
					"weight" : i.weight,
					"height" : i.height,
					"medical_history" : i.medical_history,
					"medical_problems" : i.medical_problems,
					"allergies" : i.allergies
		           }
		j+=1
	return Response(data=data,status=status.HTTP_200_OK)



@api_view(["POST"])
def update_patient(request):
	first_name = request.data["first_name"]
	last_name = request.data["last_name"]
	DOB = request.data["DOB"]
	email = request.data["email"]
	mobile = request.data["mobile"]
	gender = request.data["gender"]
	blood_group = request.data["blood_group"]
	address = request.data["address"]
	pin_code = request.data["pin_code"]
	state = request.data["state"]
	country = request.data["country"]
	weight = request.data["weight"]
	height = request.data["height"]
	medical_history = request.data["medical_history"]
	medical_problems = request.data["medical_problems"]
	allergies = request.data["allergies"]

	obj_p = Patient(
	first_name = first_name,
	last_name = last_name,
	DOB = DOB,
	email = email,
	mobile = mobile,
	gender = gender,
	blood_group = blood_group,
	address = address,
	pin_code = pin_code,
	state = state,
	country = country,
	weight = weight,
	height = height,
	medical_history = medical_history,
	medical_problems = medical_problems,
	allergies = allergies)
	obj_p.save()
	return Response(data="Data Entry Succesful",status=status.HTTP_200_OK)

@api_view(["GET"])
def api_care_taker(request):
	obj_ct = Care_Taker.objects.all()
	data = {}
	j=0
	for i in obj_ct.iterator():
		data[j] = {
					"first_name" : i.first_name,
		            "last_name": i.last_name,
					"DOB" : i.DOB,
					"email" : i.email,
					"mobile" : i.mobile,
					"gender" : i.gender,
					"address" :i.address,
					"city" :i.city,
					"pin_code" : i.pin_code,
					"state" : i.state,
					"country" : i.country,
		           }
		j+=1
	return Response(data=data,status=status.HTTP_200_OK)



@api_view(["POST"])
def update_care_taker(request):
	first_name = request.data["first_name"]
	last_name = request.data["last_name"]
	DOB = request.data["DOB"]
	email = request.data["email"]
	mobile = request.data["mobile"]
	gender = request.data["gender"]
	address = request.data["address"]
	city = request.data["city"]
	pin_code = request.data["pin_code"]
	state = request.data["state"]
	country = request.data["country"]

	obj_ct = Care_Taker(
	first_name = first_name,
	last_name = last_name,
	DOB = DOB,
	email = email,
	mobile = mobile,
	gender = gender,
	address = address,
	city = city,
	pin_code = pin_code,
	state = state,
	country = country)
	obj_ct.save()
	return Response(data="Data Entry Succesful",status=status.HTTP_200_OK)
