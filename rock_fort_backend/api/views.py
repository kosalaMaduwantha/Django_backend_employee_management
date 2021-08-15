from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse


from rest_framework import viewsets
from rest_framework.response import Response
from rock_fort_backend.models import (
  employee,
  employee_phone,
  inquiry,
  salary,
  attendance,
  task,
  event_package,
  event_offer,
  event,
  customer,
  salary,
  tour_package,
  tour


)
from .serializers import ( 
employeeSerializer,
employee_phoneSerializer,
event_packageSerializer,
taskSerializer,
event_offerSerializer,
eventSerializer,
event_packageSerializer,
customerSerializer,
salarySerializers,
tour_packageSerializer,
tourSerializer
)
from django_filters.rest_framework import DjangoFilterBackend








#class phonelistView(ListAPIView):
  #  queryset = employee_phone.objects.all()
   # serializer_class = employee_phoneSerializer

#class EmployeeDetailView(RetrieveAPIView):
 #   queryset = Employee.objects.all()
  #  serializer_class = EmployeeSerializer

#class EmployeeCreateView(CreateAPIView):
 #   queryset = Employee.objects.all()
  #  serializer_class = EmployeeSerializer

#class EmployeeDestroyView(DestroyAPIView):
 #   queryset = Employee.objects.all()
  #  serializer_class = EmployeeSerializer

# KOSALA ViewSets

class employeeViewSet(viewsets.ModelViewSet):
    serializer_class = employeeSerializer

    def get_queryset(self):
      queryset = employee.objects.all()
      return queryset

class employeeViewSetName(viewsets.ModelViewSet):
    serializer_class = employeeSerializer

    def get_queryset(self):
      queryset = employee.objects.all()
      return queryset

    lookup_field = 'fname'

class employeeViewSetDepartment(viewsets.ModelViewSet):
    serializer_class = employeeSerializer

    def get_queryset(self):
      queryset = employee.objects.all()
      return queryset

    def retrieve(self, request, *args, **kwargs):
      params = kwargs
      print(params['pk'])
      employ = employee.objects.filter(department = params['pk'])
      serializer = employeeSerializer(employ, many=True)
      return Response(serializer.data)


class employeeTasksViewSetDepartment(viewsets.ModelViewSet):
    serializer_class = taskSerializer

    def get_queryset(self):
      queryset = task.objects.all()
      return queryset

    def retrieve(self, request, *args, **kwargs):
      params = kwargs
      print(params['pk'])
      tas = task.objects.filter(status = params['pk'])
      serializer = taskSerializer(tas, many=True)
      return Response(serializer.data)

class employeeTasksViewSetEmployee(viewsets.ModelViewSet):
    serializer_class = taskSerializer

    def get_queryset(self):
      queryset = task.objects.all()
      return queryset

    def retrieve(self, request, *args, **kwargs):
      params = kwargs
      print(params['pk'])
      tas = task.objects.filter(empID = params['pk'])
      serializer = taskSerializer(tas, many=True)
      return Response(serializer.data)






class employeePhoneViewSet(viewsets.ModelViewSet):

    serializer_class = employee_phoneSerializer
    queryset = employee_phone.objects.all()
    lookup_field = 'empID_id'

class taskViewSet(viewsets.ModelViewSet):

    serializer_class = taskSerializer
    queryset = task.objects.all()


class salaryViewSet(viewsets.ModelViewSet):

    serializer_class = salarySerializers
    queryset = salary.objects.all()


# KOSALA VIEWSETS


#PRABODA

class eventPackageViewSet(viewsets.ModelViewSet):

    serializer_class = event_packageSerializer
    queryset = event_package.objects.all()

class customerViewSet(viewsets.ModelViewSet):

    serializer_class = customerSerializer
    queryset = customer.objects.all()

class eventViewSet(viewsets.ModelViewSet):

    serializer_class = eventSerializer
    queryset = event.objects.all()


class eventViewSetE(viewsets.ModelViewSet):

    serializer_class = eventSerializer

    def get_queryset(self):
      queryset = event.objects.all()
      return queryset

    def retrieve(self, request, *args, **kwargs):
      params = kwargs
      print(params['pk'])
      tas = event.objects.filter(pack_offer_type = params['pk'])
      serializer = eventSerializer(tas, many=True)
      return Response(serializer.data)



class eventOfferViewSet(viewsets.ModelViewSet):
    serializer_class = event_offerSerializer
    queryset = event_offer.objects.all()


#Kanchal

class tour_package_view(viewsets.ModelViewSet):
    serializer_class = tour_packageSerializer
    queryset = tour_package.objects.all()

class tourView(viewsets.ModelViewSet):
    serializer_class = tourSerializer
    queryset = tour.objects.all()

#Kanchal









