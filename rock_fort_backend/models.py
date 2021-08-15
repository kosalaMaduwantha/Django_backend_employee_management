from django.db import models
from django.core.validators import MaxValueValidator,RegexValidator

class room(models.Model):
    room_id = models.CharField(max_length=50, primary_key=True, unique=True, validators=[RegexValidator(r'^\d{1,10}$')])
    floor = models.CharField(max_length=100, validators=[RegexValidator(r'^\d{1,10}$')])
    room_type = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.room_id


class room_offer(models.Model):
    ro_id = models.CharField(max_length=10, primary_key=True, unique=True)
    ro_description = models.CharField(max_length=100)
    ro_price = models.FloatField()

    def __str__(self):
        return self.ro_id

class customer(models.Model):
    cID = models.CharField(max_length=50,primary_key=True, unique=True)
    fName = models.CharField(max_length=20)
    lName = models.CharField(max_length=20)
    nic = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.cID

class reservation(models.Model):
    res_id = models.CharField(max_length=10,primary_key=True, unique=True)
    room_type = models.CharField(max_length=20)
    check_in_date = models.DateField(auto_now=False, auto_now_add=False)
    check_out_date = models.DateField(auto_now=False, auto_now_add=False)
    adults = models.CharField(max_length=5, validators=[RegexValidator(r'^\d{1,10}$')])
    children = models.CharField(max_length=5, validators=[RegexValidator(r'^\d{1,10}$')])
    date_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    paid_status = models.CharField(max_length=10)
    room_id = models.ForeignKey('room', models.DO_NOTHING, default="")
    ro_id = models.ForeignKey('room_offer', models.DO_NOTHING, default="")
    cID = models.ForeignKey('customer', models.DO_NOTHING, default="")
    
    def __str__(self):
        return self.res_id

class event_package(models.Model):

    pID = models.CharField(max_length=10,primary_key=True, unique=True)
    p_category = models.CharField(max_length=20)
    e_p_description = models.CharField(max_length=100)
    e_p_price = models.FloatField()

    def __str__(self):
        return self.pID

class event(models.Model):
    eID = models.AutoField(max_length=10,primary_key=True, unique=True)
    paid_status = models.CharField(max_length=10)
    e_description = models.CharField(max_length=100)
    e_date = models.DateField(auto_now=False, auto_now_add= False)
    date_time = models.TimeField(auto_now=False, auto_now_add=False)
    pack_offer_type = models.CharField(max_length=20)
    cID = models.ForeignKey('customer', models.DO_NOTHING, default="")
    oID = models.ForeignKey('event_offer',models.DO_NOTHING, null=True, default="")
    pID = models.ForeignKey('event_package',on_delete=models.CASCADE,  null=True, default="")
 
    

    def __str__(self):
        return self.eID

class event_offer(models.Model):
    oID = models.CharField(max_length=10,primary_key=True, unique=True)
    e_o_description = models.CharField(max_length=100)
    e_price = models.FloatField()

    def __str__(self):
        return self.oID


class tour_offer(models.Model):

    offID = models.CharField(max_length=10,primary_key=True, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.offID

class tour_package(models.Model):

    packID = models.CharField(max_length=10,primary_key=True, unique=True)
    pName = models.CharField(max_length=100)
    price = models.FloatField()
    t_type = models.CharField(max_length=100)
    t_details = models.CharField(max_length=600, default='')

    def __str__(self):
        return self.packID

class tour(models.Model):

    tID = models.AutoField(max_length=10,primary_key=True, unique=True)
    booked_date = models.DateField(auto_now=False, auto_now_add=False)
    t_description = models.CharField(max_length=200)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    offID = models.ForeignKey('tour_offer',on_delete=models.CASCADE, null=True, default="")
    cID = models.ForeignKey('customer',on_delete=models.CASCADE, null=False, default="")
    packID = models.ForeignKey('tour_package',on_delete=models.CASCADE, null=False, default="")

    def __str__(self):
        return self.tID

class employee(models.Model):
    empID = models.CharField(max_length=50,primary_key=True, unique=True)
    fname = models.CharField(max_length=100, unique=True)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    nic = models.CharField(max_length=20, unique=True)

    dob = models.DateField(auto_now=False, auto_now_add=False)
    joined_date = models.DateField(auto_now=False, auto_now_add=False)
    address = models.CharField(max_length=400)
    edu_qualifications = models.CharField(max_length=400)
    prof_edu_qualifications = models.CharField(max_length=400)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.empID

class employee_phone(models.Model):
    phoneID = models.AutoField(primary_key=True)
    empID = models.ForeignKey('employee',on_delete=models.CASCADE, null=False, default="")
    employee_phone = models.CharField(max_length=10,validators=[RegexValidator(r'^\d{1,10}$')] )
    

    def __str__(self):
        return "phone from: " + str(self.empID)


class inquiry(models.Model):
    inquiryID = models.AutoField(max_length=10,primary_key=True, unique=True)
    inq_description = models.CharField(max_length=400)
    empID = models.ForeignKey('employee',on_delete=models.CASCADE, null=False, default="")

    def __str__(self):
        return self.inquiryID

class salary(models.Model):
    salaryID = models.AutoField(max_length=10,primary_key=True, unique=True)
    basic = models.FloatField()
    epf = models.FloatField()
    ot = models.FloatField()
    totalSalary = models.FloatField()
    empID = models.ForeignKey('employee',on_delete=models.CASCADE, null=False, default="")
    employee_name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.salaryID

class attendance(models.Model):
    attendanceID = models.AutoField(max_length=10,primary_key=True, unique=True)
    on_time = models.TimeField(auto_now=False, auto_now_add=False)
    off_time = models.TimeField(auto_now=False, auto_now_add=False)
    empID = models.ForeignKey('employee',on_delete=models.CASCADE, null=False, default="")

    def __str__(self):
        return self.attendanceID

class task(models.Model):
    taskID = models.AutoField(max_length=10,primary_key=True, unique=True)
    empID = models.ForeignKey('employee',on_delete=models.CASCADE, null=False, default="")
    tack_description = models.CharField(max_length=400)
    task = models.CharField(max_length=400)
    time_duration = models.CharField(max_length=50,validators=[RegexValidator(r'^\d{0,10}$')] , default=0)
    status = models.CharField(max_length=10,  default="")
    emp_name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.taskID

class supplier(models.Model):
    supplierID = models.CharField(max_length=10,primary_key=True, unique=True)
    s_company = models.CharField(max_length=100)
    s_address = models.CharField(max_length=200)
    s_type = models.CharField(max_length=100)
    s_email = models.CharField(max_length=100)

    def __str__(self):
        return self.supplierID

class inventory(models.Model):
    itemID = models.CharField(max_length=10,primary_key=True, unique=True)
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    threshold = models.FloatField()
    supplierID = models.ForeignKey('supplier', on_delete=models.CASCADE)

    def __str__(self):
        return self.itemID

class supplier_contact(models.Model):
    supplierID = models.ForeignKey('supplier', max_length=10, on_delete=models.CASCADE, unique=True)



class order(models.Model):
    orderID = models.CharField(max_length=10,primary_key=True, unique=True)
    s_company = models.CharField(max_length=100)
    s_email = models.CharField(max_length=100) 
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    amount = models.FloatField()
    supplierID = models.ForeignKey('supplier', on_delete=models.CASCADE)

    def __str__(self):
        return self.orderID

class item_order(models.Model):
    orderID = models.ForeignKey('order', on_delete=models.CASCADE)
    itemID = models.ForeignKey('inventory', on_delete=models.CASCADE)

    def __str__(self):
        return 

class budget(models.Model):
    #status = (("profit","profit"), ("lost","lost"))
    budgetID = models.CharField(max_length=10,primary_key=True, unique=True)
    timeperiod = models.DateField(auto_now=True, auto_now_add=False)
    status = models.CharField(max_length=10)
    amount = models.FloatField()

    def __str__(self):
        return self.budgetID

class expenses(models.Model):
    expensesID = models.CharField(max_length=10,primary_key=True, unique=True)
    refID = models.CharField(max_length=10)
    date_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    orderID = models.ForeignKey('order', on_delete=models.CASCADE)
    budgetID = models.ForeignKey('budget', on_delete=models.CASCADE)

    def __str__(self):
        return self.expensesID

class income(models.Model):
    income_id = models.CharField(max_length=10,primary_key=True, unique=True)
    date_time = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.income_id

class reservationPay(models.Model):
    rpay_id = models.CharField(max_length=10,primary_key=True, unique=True)
    amount = models.FloatField()
    res_id = models.ForeignKey('reservation', on_delete=models.CASCADE)
    income_id = models.ForeignKey('income', on_delete=models.CASCADE)

    def __str__(self):
        return self.rpay_id

class tourPay(models.Model):
    tpay_id = models.CharField(max_length=10,primary_key=True, unique=True)
    amount = models.FloatField()
    tID = models.ForeignKey('tour', on_delete=models.CASCADE)
    income_id = models.ForeignKey('income', on_delete=models.CASCADE)

    def __str__(self):
        return self.tpay_id

class eventPay(models.Model):
    epay_id = models.CharField(max_length=10,primary_key=True, unique=True)
    amount = models.FloatField()
    eID = models.ForeignKey('event', on_delete=models.CASCADE)
    income_id = models.ForeignKey('income', on_delete=models.CASCADE)

    def __str__(self):
        return self.epay_id








