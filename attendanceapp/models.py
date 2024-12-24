from django.db import models

# Create your models here.

class Login_model(models.Model):
    username = models.CharField(max_length=100,null=True, blank=True)
    password = models.CharField(max_length=100,null=True, blank=True)
    usertype=models.CharField(max_length=100,null=True, blank=True)
    status=models.CharField(max_length=100,null=True,blank=True)


class departrment_model(models.Model):
    department_name=models.CharField(max_length=100,null=True,blank=True)



class staff_model(models.Model):
    LOGIN_ID=models.ForeignKey(Login_model,on_delete=models.CASCADE,null=True,blank=True)
    first_name=models.CharField(max_length=100,null=True,blank=True)
    second_name=models.CharField(max_length=100,null=True,blank=True)
    DEPARTMENT=models.ForeignKey(departrment_model,on_delete=models.CASCADE,null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,blank=True)
    qualification=models.CharField(max_length=100,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    contact=models.IntegerField(null=True,blank=True)




class student_model(models.Model):
    LOGIN_ID=models.ForeignKey(Login_model,on_delete=models.CASCADE,null=True,blank=True)
    First_name=models.CharField(max_length=100,null=True,blank=True)
    Second_name=models.CharField(max_length=100,null=True,blank=True)
    Department=models.ForeignKey(departrment_model,on_delete=models.CASCADE,null=True,blank=True)
    Age=models.IntegerField(null=True,blank=True)
    Gender=models.CharField(max_length=100,null=True,blank=True)


class Complaint_model(models.Model):
    STUDENT_ID = models.ForeignKey(student_model, on_delete=models.CASCADE, null=True, blank=True)
    complaint=models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    reply=models.CharField(max_length=100,null=True,blank=True)


class notification_model(models.Model):
    STUDENT_ID = models.ForeignKey(student_model, on_delete=models.CASCADE, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    message=models.CharField(max_length=100,null=True,blank=True)

class subject_model(models.Model):
    STUDENT_ID = models.ForeignKey(student_model, on_delete=models.CASCADE, null=True, blank=True)
    subject=models.CharField(max_length=100,null=True,blank=True)
    staff=models.CharField(max_length=100,null=True,blank=True)
    DEPARTMENT=models.ForeignKey(departrment_model,on_delete=models.CASCADE,null=True,blank=True)
    period=models.IntegerField(null=True,blank=True)


class attendence_model(models.Model):
    STUDENTID = models.ForeignKey(student_model,on_delete=models.CASCADE, null=True, blank=True)
    attendance=models.CharField(max_length=100,null=True,blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)        


class leave_model(models.Model):
    request=models.CharField(max_length=100,null=True,blank=True)
    date=models.CharField(max_length=100,null=True,blank=True)
    STUDENTID = models.ForeignKey(student_model,on_delete=models.CASCADE, null=True, blank=True)
               