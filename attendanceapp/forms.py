from django.forms import ModelForm

from .models import *


class Add_dept_form(ModelForm):
    class Meta:
        model=departrment_model
        fields=['department_name']

class Add_notification_form(ModelForm):
    class Meta:
        model = notification_model
        fields=['message']


class Add_student_form(ModelForm):
    class Meta:
        model = student_model
        fields=['First_name', 'Second_name', 'Department','Age','Gender' ]



class Add_staff_form(ModelForm):
    class Meta:
        model = staff_model
        fields=['first_name','second_name','gender','qualification','age','contact' ]