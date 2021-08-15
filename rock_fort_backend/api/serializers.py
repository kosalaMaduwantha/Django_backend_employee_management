from rest_framework import serializers
from rock_fort_backend.models import (
employee, 
employee_phone,
event_package,
task,
customer,
event,
event_offer,
customer,
salary,
tour_package,
tour

)


#KOSALA serializers
class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = ['empID','fname','lname','nic','dob','joined_date','address','edu_qualifications','prof_edu_qualifications','designation','department','gender']


class employee_phoneSerializer(serializers.ModelSerializer):
    class Meta:
        model =  employee_phone
        fields = ['phoneID','empID', 'employee_phone']


class taskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = ['taskID','empID','tack_description','task','time_duration','status','emp_name']

class salarySerializers(serializers.ModelSerializer):
    class Meta:
        model = salary
        fields = ['salaryID','basic','epf','ot','totalSalary','empID','employee_name']

#KOSALA serializers

#PRABODA


class event_packageSerializer(serializers.ModelSerializer):
    class Meta:
        model = event_package
        fields = ['pID','p_category','e_p_description','e_p_price']

class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = ['cID', 'fName', 'lName', 'nic', 'email', 'phone', 'country']

class eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = event
        fields = ['eID', 'paid_status', 'e_description','e_date','date_time' , 'pack_offer_type' , 'cID', 'oID', 'pID']

class event_offerSerializer(serializers.ModelSerializer):
        class Meta:
            model = event_offer
            fields  = ['oID', 'e_o_description', 'e_price']

#Kanchal

class tour_packageSerializer(serializers.ModelSerializer):
        class Meta:
            model = tour_package
            fields = ['packID','pName','price','t_type','t_details']

class tourSerializer(serializers.ModelSerializer):
        class Meta:
            model = tour
            fields = ['tID','booked_date','t_description','time','offID','cID','packID']

#Kanchal
