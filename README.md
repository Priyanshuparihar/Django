1st clone this repo
- cd Django
- pip install requirements.txt
- python manage.py runserver

![image](https://user-images.githubusercontent.com/55618725/157670382-35644a86-32db-496b-ac00-4bcb6b298e0b.png)

here you find the link
example : http://127.0.0.1:8000/api_sensor

### API 1 : /api_sensor
- To see the API response.

### API 2 : /update_sensor
{
"oximeter": 89.0,
"temp": 45.0
}

### API 3 : /api_patient
- To see the API response. 

### API 4 : /update_patient
{
    "first_name": "Priya",
    "last_name": "Parihar",
    "DOB": "2022-03-06",
    "email": "pp@gmail.com",
    "mobile": "9024590008",
    "gender": "male",
    "blood_group": "B+",
    "address": "Jai Narayan Vyas Colony, ChandPole",
    "pin_code": 342001,
    "state": "Rajasthan",
    "country": "India",
    "weight": 80.0,
    "height": 5.6,
    "medical_history": "Nope",
    "medical_problems": "NA",
    "allergies": "NA"
}

### API 5 : /api_care_taker
- To see the API response.

### API 6 : /update_care_taker
{
    "first_name": "Priyanshu",
    "last_name": "Parihar",
    "DOB": "2022-03-15",
    "email": "pp@gmail.com",
    "mobile": "861942000",
    "gender": "Male",
    "address": "Baba Ramdev Chowk",
    "city": "Jodhpur",
    "pin_code": 342001,
    "state": "Rajasthan",
    "country": "Japan"
}

### API 7 : /api_doctor
- To see the API response.

### API 8 : /update_doctor
{
    "name": "Priyanshu Parihar",
    "age": 39,
    "email": "p@gmail.com",
    "experience": 6,
    "designation": "sr. doctor",
    "mobile": "8619420000",
    "hospital_name": "MMD",
    "hospital_address": "Vyas Colony, ChandPole"
}
