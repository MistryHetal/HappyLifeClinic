from django.db import models
from django.contrib import admin 
from django.db.models.deletion import CASCADE

# Create your models here.

class city(models.Model):
    city_name = models.CharField(max_length=50)
    def __str__(self):
        return  self.city_name

class cityAdmin(admin.ModelAdmin):
    list_display = ('city_name',)
    ordering = ('city_name',)
    search_fields = ('city_name',)

class area(models.Model):
    area_name = models.CharField(max_length=50)
    city_id = models.ForeignKey(city, on_delete=models.CASCADE)

    def __str__(self):
        return  self.area_name

class areaAdmin(admin.ModelAdmin):
    list_display = ('area_name',)
    ordering = ('area_name',)
    search_fields = ('area_name',)

class clinic(models.Model):
    clinic_name = models.CharField(max_length=50)
    clinic_address = models.CharField(max_length=150)
    clinic_Connum = models.CharField(max_length=150)
    clinic_email = models.EmailField()
    def __str__(self):
        return  self.clinic_name

class clinicAdmin(admin.ModelAdmin):
    list_display = ('clinic_name','clinic_address', 'clinic_Connum', 'clinic_email')
    ordering = ('clinic_name',)
    search_fields = ('clinic_name','clinic_email')


class treatement(models.Model):
    treatement_type = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    prescription = models.CharField(max_length=50)
    def __str__(self):
        return  self.treatement_type

class treatementAdmin(admin.ModelAdmin):
    list_display = ('treatement_type','description', 'prescription')
    ordering = ('treatement_type',)
    search_fields = ('treatement_type','prescription')

class event(models.Model):
    event_sdate = models.DateField()
    event_edate = models.DateField()
    event_type = models.CharField(max_length=50)
    event_desc = models.CharField(max_length=100)
    def __str__(self):
        return  self.event_type

class eventAdmin(admin.ModelAdmin):
    list_display = ('event_type','event_sdate','event_edate','event_desc')
    ordering = ('event_type',)
    search_fields = ('event_type','event_desc')

class appointment(models.Model):
    appointment_charge = models.IntegerField(null=True)
    appointment_status = models.CharField(max_length=45, null=True)
    cancel_appointment = models.BooleanField(default="Not Specified")
    def __str__(self):
        return  self.appointment_status

class clinicappointment(admin.ModelAdmin):
    list_display = ('appointment_status','appointment_charge','cancel_appointment')
    ordering = ('appointment_status',)
    search_fields = ('appointment_status','cancel_appointment')

class schedule(models.Model):
    schedule_date = models.DateField()
    schedule_stime = models.TimeField()
    schedule_etime = models.TimeField()
    def __str__(self) -> str:
        return f'{self.schedule_date}'

class scheduleAdmin(admin.ModelAdmin):
    list_display =  ('schedule_date','schedule_stime', 'schedule_etime')
    ordering = ('schedule_date',)
    search_fields = ('schedule_date','schedule_stime')

class medicine(models.Model):
    medicine_name = models.CharField(max_length=50)
    medicine_price = models.IntegerField()
    medicine_qty = models.IntegerField()
    medicine_desc = models.CharField(max_length=150)
    medicine_exdate = models.DateField()
    def __str__(self):
        return  self.medicine_name

class medicineAdmin(admin.ModelAdmin):
    list_display = ('medicine_name','medicine_price', 'medicine_qty', 'medicine_desc', 'medicine_exdate')
    ordering = ('medicine_name',)
    search_fields = ('madicine_name','madicine_price')

class feedback(models.Model):
    feedback_date = models.DateField()
    feedback_desc = models.CharField(max_length=150)
    def __str__(self):
        return  self.feedback_desc

class feedbackAdmin(admin.ModelAdmin):
    list_display = ('feedback_date','feedback_desc')
    ordering = ('feedback_date',)
    search_fields = ('feedback_date','feedback_desc')

class payment(models.Model):
    payment_date = models.DateField(auto_now_add=True)
    payment_method = models.CharField( max_length=5, default="Individual")
    payment_amount = models.IntegerField()
    payment_receiptnum = models.IntegerField()

    def __str__(self):
        return "Payment user-{} Amount-{}".format(self.payment_id, self.payment_amount)

class paymentAdmin(admin.ModelAdmin):
    list_display = ('payment_date','payment_method', 'payment_amount', 'payment_receiptnum')
    ordering = ('payment_date',)
    search_fields = ('payment_date','payment_method', 'payment_receiptnum')

class diagnosis(models.Model):
    diagnosis_details = models.CharField(max_length=200)
    ordering = ('diagnosis_details',)
    search_fields = ('diagnosis_details',)
    def __str__(self):
        return  self.diagnosis_details

class diagnosisAdmin(admin.ModelAdmin):
    list_display = ('diagnosis_details',)
    ordering = ('diagnosis_details',)
    search_fields = ('diagnosis_details',)

class report(models.Model):
    report_name = models.CharField(max_length=50)
    ordering = ('report_name',)
    search_fields = ('report_name',)
    def __str__(self):
        return  self.report_name

class reportAdmin(admin.ModelAdmin):
    list_display = ('report_name',)
    ordering = ('report_name',)
    search_fields = ('report_name',)

class role(models.Model):
    role_name = models.CharField(max_length=50) 
    ordering = ('role_name',)
    search_fields = ('role_name',)
    def __str__(self):
        return  self.role_name

class roleAdmin(admin.ModelAdmin):
    list_display = ('role_name',)
    ordering = ('role_name',)
    search_fields = ('role_name',)
