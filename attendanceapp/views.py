from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from .forms import *

from .models import *

# Create your views here.

class login_page(View):
    def get(self,request):
        return render(request,'hod/hodlogin.html')   
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        login_obj=Login_model.objects.get(username=username,password=password)
        if login_obj.usertype=="admin":
            return HttpResponse('''<script>alert("welcome to a");window.location="/dashboard"</script>''')
    
# //////////////////////////////////////////////// ADMIN //////////////////////////////////////////

class Add_staff(View):
    def get(self, request):
        obj=departrment_model.objects.all()
        return render(request, 'administrator/add-staff.html',{'val':obj})
    def post(self,request):
        c=Add_staff_form(request.POST)
        if c.is_valid():
            f=c.save(commit=False)
            obj = Login_model.objects.create(username=request.POST['username'], password=request.POST['password'],usertype="staff")
            dept=departrment_model.objects.get(id=request.POST['Department'])
            print(dept)
            f.Department=dept
            f.LOGIN_ID=obj
            f.save()
            return HttpResponse('''<script>alert("staff added");window.location="/managestaff"</script>''')
    

class Add_dept(View):
    def get(self,request):
        return render(request, 'administrator/add_dept.html')
    def post(self,request):
        c= Add_dept_form(request.POST)
        if c.is_valid():
            c.save()
            return HttpResponse('''<script>alert("dept added");window.location="/managedept"</script>''')
    


class Add_notification(View):
    def get(self,request):
        return render(request,'administrator/add-notification.html')    
    def post(self,request):
        c=Add_notification_form(request.POST)
        if c.is_valid():
            c.save()
            return HttpResponse('''<script>alert("notification added");window.location="/managenotification"</script>''')

class Add_student(View):
    def get(self,request):
        obj =departrment_model.objects.all()
        return render(request,'administrator/add-student.html',{'dept':obj})
    def post(self,request):
        c=Add_student_form(request.POST)
        if c.is_valid():
            f=c.save(commit=False)
            obj = Login_model.objects.create(username=request.POST['username'], password=request.POST['password'],usertype="student")
            dept=departrment_model.objects.get(id=request.POST['Department'])
            f.Department=dept
            f.LOGIN_ID=obj
            f.save()
            return HttpResponse('''<script>alert("student added");window.location="/managestudent"</script>''')


class Admin_dashboard(View):
    def get(self,request):
        return render(request,'administrator/dashboard.html')    
    

class Edit_dept(View):
    def get(self,request):
        return render(request,'administrator/edit_dept.html')   


class Edit_staff(View):
    def get(self,request, pk):
        obj = staff_model.objects.get(id=pk)
        return render(request,'administrator/edit-staff.html',{'a':obj})  
    


class Edit_student(View):
    def get(self,request):
        return render(request,'administrator/edit-students.html') 


class Manage_department(View):
    def get(self,request):
        c=departrment_model.objects.all()
        return render(request,'administrator/manage-department.html',{'obj':c})


class Manage_staff(View):
    def get(self,request):
        obj =staff_model.objects.all()
        return render(request,'administrator/manage-staff.html',{'obj':obj})



class Manage_student(View):
    def get(self,request):
        c=student_model.objects.all()
        return render(request,'administrator/manage-student.html',{'obj':c})   



class Reply_complaints(View):
    def get(self,request):
        return render(request,'administrator/Reply_complaint.html')    
    


class View_complaint_send_reply(View):
    def get(self,request):
        return render(request,'administrator/view-complaint-send-reply.html')   
    

class manage_notification(View):
    def get(self, request):
        c=notification_model.objects.all()
        return render(request, 'administrator/manage_notification.html',{'obj':c})
    
class deletenotification(View):
    def get(self,request, pk):
        c=notification_model.objects.get(id=pk)
        c.delete()
        return redirect('managenot')
    


class deletedept(View):
    def get(self,request, pk):
        c=departrment_model.objects.get(id=pk)
        print(c)
        c.delete()
        return HttpResponse('''<script>alert("deleted successfully");window.location="/managedept"</script>''')
    

class deletestudent(View):
    def get(self,request, pk):
        c=student_model.objects.get(id=pk)
        print(c)
        c.delete()
        return HttpResponse('''<script>alert("deleted successfully");window.location="/managestudent"</script>''')


class deletestaff(View):
    def get(self,request, pk):
        c=staff_model.objects.get(id=pk)
        print(c)
        c.delete()
        return HttpResponse('''<script>alert("deleted successfully");window.location="/managestaff"</script>''')



    # ////////////////////////////////////////// HOD///////////////////////////////// 


class Approve_daily_leave(View):
    def get(self,request):
        return render(request,'hod/approve_daily_leave.html')   
    

class Change_password(View):
    def get(self,request):
        return render(request,'hod/changepassword.html')   
    

class Hoddash(View):
    def get(self,request):
        return render(request,'hod/hoddash.html')   
    


class Manage_subject_allocated(View):
    def get(self,request):
        return render(request,'hod/manage_subject_allocated.html')   
    

class Notification(View):
    def get(self,request):
        return render(request,'hod/manage-niotification.html')   
    

class Manage_subjects(View):
    def get(self,request):
        return render(request,'hod/manage-subjects.html')   
    

class View_attendence_marked(View):
    def get(self,request):
        return render(request,'hod/view_attendence_marked.html')   
    

class View_profile(View):
    def get(self,request):
        return render(request,'hod/view-profile.html')   
    

    #////////////////////////////teacher///////////////////////////////////////


class Change_password(View):
    def get(self,request):
        return render(request,'teacher/change_password.html')   
class Handle_correction_request(View):
    def get(self,request):
        return render(request,'teacher/handle_correction_request.html')   
class Teacherdash(View):
    def get(self,request):
        return render(request,'teacher/teacherdash.html')   
class Teacherlogin(View):
    def get(self,request):
        return render(request,'teacher/teacherlogn.html')   
class View_attendence_marked(View):
    def get(self,request):
        return render(request,'teacher/view_attendence_marked.html')   
class Notification(View):
    def get(self,request):
        return render(request,'teacher/view_notification.html')   
class Deptwise_staffandstudent(View):
    def get(self,request):
        return render(request,'teacher/dept_staffandstudent.html')   
class Subject_allocated(View):
    def get(self,request):
        return render(request,'teacher/view-subject-allocated.html')   
class Viewandedit_profile(View):
    def get(self,request):
        return render(request,'teacher/viewandedit_profile.html')   



