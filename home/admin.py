from django.contrib import admin
from home.models import *

# Register your models here.
admin.site.register(city,cityAdmin)
admin.site.register(area,areaAdmin)
admin.site.register(clinic, clinicAdmin)
admin.site.register(appointment, clinicappointment)
admin.site.register(event, eventAdmin)
admin.site.register(medicine, medicineAdmin)
admin.site.register(treatement, treatementAdmin)
admin.site.register(diagnosis, diagnosisAdmin)
admin.site.register(schedule, scheduleAdmin)
admin.site.register(role,roleAdmin)
admin.site.register(report,reportAdmin)
admin.site.register(payment,paymentAdmin)
admin.site.register(feedback,feedbackAdmin)
