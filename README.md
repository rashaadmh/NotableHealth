# NotableHealth
 
Run in virtual env with python > 3.6

Run `pip install -r requirements.txt`


Intitialize database by running `./manage.py migrate`


To start server, run `./manage.py runserver`

Endpoints:

GET

http://127.0.0.1:8000/get_doctors/

-Retrieve list of doctors

-No parameters needed

GET

http://127.0.0.1:8000/get_appointments?

-Retrieve list of appointments for a given doctor and date

-Query Params:

	-doctor_uuid
    	-date
        	-should be in format "%Y-%m-%d"

Example: http://127.0.0.1:8000/get_appointments?doctor_uuid=cf6f9403-e23d-4d3e-bafa-b05ddcc495c7&date=2020-10-26

DEL

http://127.0.0.1:8000/delete_appointment?

-Delete an appointment with given appointment uuid

-Query Params:
	-appointment_uuid

Example:
http://127.0.0.1:8000/delete_appointment?appointment_uuid=6cd0b894-aea9-44c3-bbf8-fb0c77bb49a9

POST

http://127.0.0.1:8000/create_appointment/

-Schedule an appointment

-Body example:

``{
	"doctor_uuid":"cf6f9403-e23d-4d3e-bafa-b05ddcc495c7",
	"datetime":"2020-10-25 08:15", # in form of '%Y-%m-%d %H:%M'
	"patient_first_name":"troy",
	"patient_last_name":"barnes",
	"kind":"follow_up"
}``

POST 

HTTP://127.0.0.1:800/create_doctor/

-Create a doctor

-Body example:

``{
    "first_name":"Will",
    "last_name":"Smith"
}``
