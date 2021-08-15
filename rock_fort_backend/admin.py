from django.contrib import admin

# Register your models here.
from .models import (
    room,
    room_offer,
    customer,
    reservation,
    event_package,
    event,
    event_offer,
    tour_offer,
    tour_package,
    tour,
    employee,
    employee_phone,
    inquiry,
    salary,
    attendance,
    task,
    supplier,
    inventory,
    supplier_contact,
    order,
    item_order,
    budget,
    expenses,
    income,
    reservationPay,
    tourPay,
    eventPay,


)

admin.site.register(room)
admin.site.register(room_offer)
admin.site.register(customer)
admin.site.register(reservation)
admin.site.register(event_package)
admin.site.register(event)
admin.site.register(event_offer)
admin.site.register(tour_offer)
admin.site.register(tour_package)
admin.site.register(tour)
admin.site.register(employee)
admin.site.register(employee_phone)
admin.site.register(inquiry)
admin.site.register(salary)
admin.site.register(attendance)
admin.site.register(task)
admin.site.register(supplier)
admin.site.register(inventory)
admin.site.register(supplier_contact)
admin.site.register(order)
admin.site.register(item_order)
admin.site.register(budget)
admin.site.register(expenses)
admin.site.register(income)
admin.site.register(reservationPay)
admin.site.register(tourPay)
admin.site.register(eventPay)


