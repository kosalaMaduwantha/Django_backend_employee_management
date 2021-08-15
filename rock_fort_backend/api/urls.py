
from rock_fort_backend.api.views import(
employeeViewSet,
employeePhoneViewSet,eventPackageViewSet,
employeeViewSetDepartment,
taskViewSet,employeeViewSetName,
employeeTasksViewSetDepartment,
customerViewSet,eventViewSet,
eventOfferViewSet,
eventViewSetE,
employeeTasksViewSetEmployee,
salaryViewSet,
tour_package_view,
tourView

)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

#KOSALA URLS
router.register(r'employee', employeeViewSet, basename='employee')
router.register(r'employeeD', employeeViewSetDepartment, basename='employee_department')
router.register(r'phone', employeePhoneViewSet, basename= 'employee_phone')
router.register(r'task', taskViewSet, basename="task")
router.register(r'employeeName', employeeViewSetName, basename='Employee_name')
router.register(r'taskC', employeeTasksViewSetDepartment, basename='completed tasks')
router.register(r'taskCEmployee', employeeTasksViewSetEmployee, basename='tasks of employees')
router.register(r'salary', salaryViewSet, basename='salary' )


#KOSALA URLS

#PRABODA
router.register(r'eventPackage', eventPackageViewSet, basename='eventPackage')
router.register(r'customer', customerViewSet, basename='customer')
router.register(r'event', eventViewSet, basename='event')
router.register(r'eventE', eventViewSetE, basename='event')
router.register(r'eventOffer' , eventOfferViewSet, basename='eventOffer')



#Kanchal

router.register(r'tourPackage',tour_package_view,basename='tour_package')
router.register(r'tour',tourView,basename='tour')

#kanchal




urlpatterns = router.urls





#from django.urls import path
#from .views import (
 #   EmployeelistView, 
  #  EmployeeDetailView,
   # EmployeeCreateView,
   # EmployeeDestroyView
#)


#urlpatterns = [
 #   path('', EmployeelistView.as_view()),
  #  path('create/', EmployeeCreateView.as_view()),
   # path('<pk>', EmployeeDetailView.as_view()),
   # path('<pk>/delete', EmployeeDestroyView.as_view())
    

#]

