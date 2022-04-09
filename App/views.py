from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

def index(request):
	obj_p = Patient.objects.all()[0]
	data = {"Patient": obj_p}
	return render(request, "index.html", data)

def profile(request):
	return render(request, "myProfile.html")

@csrf_exempt
def ProfileEdit(request):
	return render(request, "myProfileEdit.html")

def weeklyRecord(request):
	return render(request, "WeeklyRecord.html")

def doctorDetails(request):
	return render(request, "doctorDetails.html")

def editDoctorDetails(request):
	return render(request, 'editDoctorDetails.html')

def careTaker(request):
	return render(request, 'careTakerDetails.html')

def editCareTaker(request):
	return render(request, 'editCareTaker.html')

@api_view(["GET","POST"])
def api_sensor(request):
	if(request.method == "GET"):
		try:
			t = Sensor.objects.all()
			# data = "yes"
			data = {}
			j=0
			
			for i in t.iterator():
				data[j] = {
							"Time" : i.time.strftime("%Y-%m-%d %H:%M:%S"), 
							"Oximeter" : i.oximeter, 
							"Temperature" : i.temp
						}
				j+=1
			return Response(data=data,status=status.HTTP_200_OK)

		except:
			data = {'ERROR' : "Data not Found."}
			return Response(data=data,status=status.HTTP_404_NOT_FOUND)
	elif(request.method == "POST"):
		try:
			oximeter = request.data["oximeter"]
			temp = request.data["temp"]
			t = Sensor(oximeter=oximeter, temp=temp)
			t.save()
			return Response(data="Data Entry Succesful",status=status.HTTP_200_OK)
		except:
			data = {'ERROR' : "Enter Valid Data"}
			return Response(data=data,status=status.HTTP_406_NOT_ACCEPTABLE)



# @api_view(["POST"])
# def update_sensor(request):
# 	try:
# 		oximeter = request.data["oximeter"]
# 		temp = request.data["temp"]
# 		t = Sensor(oximeter=oximeter, temp=temp)
# 		t.save()
# 		return Response(data="Data Entry Succesful",status=status.HTTP_200_OK)
# 	except:
# 		data = {'ERROR' : "Enter Valid Data"}
# 		return Response(data=data,status=status.HTTP_406_NOT_ACCEPTABLE)




@api_view(["GET","POST"])
def api_patient(request):
	if(request.method == "GET"):
		try:
			obj_p = Patient.objects.all()[0]
			data ={
					"first_name" : obj_p.first_name,
					"last_name": obj_p.last_name,
					"DOB" : obj_p.DOB,
					"email" : obj_p.email,
					"mobile" : obj_p.mobile,
					"gender" : obj_p.gender,
					"blood_group" : obj_p.blood_group,
					"address" :obj_p.address,
					"pin_code" : obj_p.pin_code,
					"state" : obj_p.state,
					"city":obj_p.city,
					"country" : obj_p.country,
					"weight" : obj_p.weight,
					"height" : obj_p.height,
					"medical_history" : obj_p.medical_history,
					"medical_problems" : obj_p.medical_problems,
					"allergies" : obj_p.allergies
					}
			return Response(data=data,status=status.HTTP_200_OK)
		
		except:
			data = {'ERROR' : "Data not Found."}
			return Response(data=data,status=status.HTTP_404_NOT_FOUND)

	elif(request.method == "POST"):
    	
		try:
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
			city = request.data["city"]
			country = request.data["country"]
			weight = request.data["weight"]
			height = request.data["height"]
			medical_history = request.data["medical_history"]
			medical_problems = request.data["medical_problems"]
			allergies = request.data["allergies"]

			obj_p = Patient(0,
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
			city=city,
			country = country,
			weight = weight,
			height = height,
			medical_history = medical_history,
			medical_problems = medical_problems,
			allergies = allergies)
			obj_p.save()
			return Response(data="Data Entry Succesful",status=status.HTTP_200_OK)
		except:
			data = {'ERROR' : "Enter Valid Data"}
			return Response(data=data,status=status.HTTP_406_NOT_ACCEPTABLE)




# @api_view(["POST"])
# def update_patient(request):
# 	try:
# 		first_name = request.data["first_name"]
# 		last_name = request.data["last_name"]
# 		DOB = request.data["DOB"]
# 		email = request.data["email"]
# 		mobile = request.data["mobile"]
# 		gender = request.data["gender"]
# 		blood_group = request.data["blood_group"]
# 		address = request.data["address"]
# 		pin_code = request.data["pin_code"]
# 		state = request.data["state"]
# 		country = request.data["country"]
# 		weight = request.data["weight"]
# 		height = request.data["height"]
# 		medical_history = request.data["medical_history"]
# 		medical_problems = request.data["medical_problems"]
# 		allergies = request.data["allergies"]

# 		obj_p = Patient(0,
# 		first_name = first_name,
# 		last_name = last_name,
# 		DOB = DOB,
# 		email = email,
# 		mobile = mobile,
# 		gender = gender,
# 		blood_group = blood_group,
# 		address = address,
# 		pin_code = pin_code,
# 		state = state,
# 		country = country,
# 		weight = weight,
# 		height = height,
# 		medical_history = medical_history,
# 		medical_problems = medical_problems,
# 		allergies = allergies)
# 		obj_p.save()
# 		return Response(data="Data Entry Succesful",status=status.HTTP_200_OK)
# 	except:
# 		data = {'ERROR' : "Enter Valid Data"}
# 		return Response(data=data,status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(["GET","POST"])
def api_care_taker(request):
	if(request.method == "GET"):
		try:
			obj_ct = Care_Taker.objects.all()[0]
			data = {
					"first_name" : obj_ct.first_name,
					"last_name": obj_ct.last_name,
					"DOB" : obj_ct.DOB,
					"email" : obj_ct.email,
					"mobile" : obj_ct.mobile,
					"gender" : obj_ct.gender,
					"address" :obj_ct.address,
					"city" :obj_ct.city,
					"pin_code" : obj_ct.pin_code,
					"state" : obj_ct.state,
					"country" : obj_ct.country
					}
			return Response(data=data,status=status.HTTP_200_OK)
		except:
			data = {'ERROR' : "Data not Found."}
			return Response(data=data,status=status.HTTP_404_NOT_FOUND)
	
	elif(request.method == "POST"):	
    
		try:
			
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

			obj_ct = Care_Taker(0,
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
		except:
			data = {'ERROR' : "Enter Valid Data"}
			return Response(data=data,status=status.HTTP_406_NOT_ACCEPTABLE)



# @api_view(["POST"])
# def update_care_taker(request):
# 	try:
# 		first_name = request.data["first_name"]
# 		last_name = request.data["last_name"]
# 		DOB = request.data["DOB"]
# 		email = request.data["email"]
# 		mobile = request.data["mobile"]
# 		gender = request.data["gender"]
# 		address = request.data["address"]
# 		city = request.data["city"]
# 		pin_code = request.data["pin_code"]
# 		state = request.data["state"]
# 		country = request.data["country"]

# 		obj_ct = Care_Taker(0,
# 		first_name = first_name,
# 		last_name = last_name,
# 		DOB = DOB,
# 		email = email,
# 		mobile = mobile,
# 		gender = gender,
# 		address = address,
# 		city = city,
# 		pin_code = pin_code,
# 		state = state,
# 		country = country)
# 		obj_ct.save()
# 		return Response(data="Data Entry Succesful",status=status.HTTP_200_OK)
# 	except:
# 		data = {'ERROR' : "Enter Valid Data"}
# 		return Response(data=data,status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(["GET","POST"])
def api_doctor(request):
	if(request.method == "GET"):
		try:
			obj_d = Doctor.objects.all()[0]
			data = {"name" : obj_d.name, 
					"age" : obj_d.age, 
					"email" : obj_d.email, 
					"experience" : obj_d.experience,
					"designation" : obj_d.designation,
					"mobile" : obj_d.mobile, 
					"hospital_name" : obj_d.hospital_name, 
					"hospital_address" : obj_d.hospital_address
					}
			return Response(data=data,status=status.HTTP_200_OK)
		except:
			data = {'ERROR' : "Data not Found."}
			return Response(data=data,status=status.HTTP_404_NOT_FOUND)
	elif(request.method == "POST"):	
		try:
			name = request.data["name"]
			age = request.data["age"]
			email = request.data["email"]
			experience = request.data["experience"]
			designation = request.data["designation"]
			mobile = request.data["mobile"]
			hospital_name = request.data["hospital_name"]
			hospital_address = request.data["hospital_address"]

			obj_d = Doctor(0,
			name = name,
			age = age,
			email = email,
			experience = experience,
			designation = designation,
			mobile = mobile,
			hospital_name = hospital_name,
			hospital_address = hospital_address)
			obj_d.save()
			return Response(data="Data Entry Succesful",status=status.HTTP_200_OK)
		except:
			data = {'ERROR' : "Enter Valid Data"}
			return Response(data=data,status=status.HTTP_406_NOT_ACCEPTABLE)

# @api_view(["POST"])
# def update_doctor(request):
# 	try:
# 		name = request.data["name"]
# 		age = request.data["age"]
# 		email = request.data["email"]
# 		experience = request.data["experience"]
# 		designation = request.data["designation"]
# 		mobile = request.data["mobile"]
# 		hospital_name = request.data["hospital_name"]
# 		hospital_address = request.data["hospital_address"]

# 		obj_d = Doctor(0,
# 		name = name,
# 		age = age,
# 		email = email,
# 		experience = experience,
# 		designation = designation,
# 		mobile = mobile,
# 		hospital_name = hospital_name,
# 		hospital_address = hospital_address)
# 		obj_d.save()
# 		return Response(data="Data Entry Succesful",status=status.HTTP_200_OK)
# 	except:
# 		data = {'ERROR' : "Enter Valid Data"}
# 		return Response(data=data,status=status.HTTP_406_NOT_ACCEPTABLE)