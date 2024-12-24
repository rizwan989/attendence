from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Login_model)
admin.site.register(departrment_model)
admin.site.register(staff_model)
admin.site.register(student_model)
admin.site.register(Complaint_model)
admin.site.register(notification_model)
admin.site.register(subject_model)
admin.site.register(attendence_model)
admin.site.register(leave_model)
