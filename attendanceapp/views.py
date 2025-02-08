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
        elif login_obj.usertype=="hod":
            return HttpResponse('''<script>alert("welcome to a");window.location="/hoddash"</script>''')
        

class logout(View):
    def get(self,request):
        return HttpResponse('''<script>alert("logout successfully");window.location='/'</script>''')
    
# //////////////////////////////////////////////// ADMIN //////////////////////////////////////////

class Add_staff(View):
    def get(self, request):
        obj=departrment_model.objects.all()
        return render(request, 'administrator/add-staff.html',{'val':obj})
    def post(self,request):
        c=Add_staff_form(request.POST)
        if c.is_valid():
            f=c.save(commit=False)
            obj = Login_model.objects.create(username=request.POST['username'], password=request.POST['password'],usertype=request.POST['usertype'])
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
            f.LOGIN_ID=obj
            f.save()
            return HttpResponse('''<script>alert("student added");window.location="/managestudent"</script>''')


class Admin_dashboard(View):
    def get(self,request):
        return render(request,'administrator/dashboard.html')    
    

class Edit_dept(View):
    def get(self,request, pk):
        obj = departrment_model.objects.get(id=pk)
        return render(request,'administrator/edit_dept.html',{'c':obj}) 
    def post(self,request,pk):
        c=departrment_model.objects.get(id=pk)
        b=Add_dept_form(request.POST,instance=c)
        if b.is_valid():
            b.save()
            return HttpResponse('''<script>alert("department updated");window.location="/managedept"</script>''')  


class Edit_staff(View):
    def get(self,request, pk):
        obj = staff_model.objects.get(id=pk)
        d=departrment_model.objects.all()
        return render(request,'administrator/edit-staff.html',{'a':obj, 'c':d})  
    def post(self,request,pk):
        c=staff_model.objects.get(id=pk)
        b=Add_staff_form(request.POST,instance=c)
        if b.is_valid():
            b.save()
            return HttpResponse('''<script>alert("staff updated");window.location="/managestaff"</script>''')

    


class Edit_student(View):
    def get(self,request,pk):
        obj = student_model.objects.get(id=pk)
        d=departrment_model.objects.all()
        return render(request,'administrator/edit-students.html',{'i':obj, 'c':d}) 
    def post(self,request,pk):
        c=student_model.objects.get(id=pk)
        b=Add_student_form(request.POST,instance=c)
        if b.is_valid():
            b.save()
            return HttpResponse('''<script>alert("students updated");window.location="/managestudent"</script>''')

    


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
    def get(self,request,pk):
        obj = Complaint_model.objects.get(id=pk)
        return render(request,'administrator/Reply_complaint.html',{'i':obj})    
    def post(self,request,pk):
        c=Complaint_model.objects.get(id=pk)
        b=reply_form(request.POST,instance=c)
        if b.is_valid():
            b.save()
            return HttpResponse('''<script>alert("complaint replied");window.location="/viewcomplaintssendreply"</script>''')
    


class View_complaint_send_reply(View):
    def get(self,request):
        c=Complaint_model.objects.all()
        return render(request,'administrator/view-complaint-send-reply.html',{'obj':c},)   
    

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
        c=leave_model.objects.all()
        return render(request,'hod/approve_daily_leave.html',{'obj1':c})   
    
class Accept_leave(View):
    def get(self, request, C_id):
            lev = leave_model.objects.filter(id=C_id).first()
            print(lev)  # Fetch the instance
            lev.leavestatus = 'Approve'  # Update the status
            lev.save()  # Save the changes
            return HttpResponse('''<script>alert("Accepted");window.location="/approve"</script>''')  
    
class Reject_leave(View):
    def get(self, request, C_id):
            lev = leave_model.objects.get(id=C_id)
            print(lev)  # Fetch the instance
            lev.leavestatus = 'Reject'  # Update the status
            lev.save()  # Save the changes
            return HttpResponse('''<script>alert("rejected");window.location="/approve"</script>''')  
        
        

    

class Manage_subjects(View):
    def get(self,request):
     obj1=subject_model.objects.all()
     return render(request,'hod/manage-subjects.html',{'obj1':obj1})
    
    
    
class add_subject (View):
    def get(self,request):
        obj1=departrment_model.objects.all()
        return render(request,'hod/add_subject.html',{'obj1':obj1})
    def post(self,request):
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("subject added successfully");window.location="/subject"</script>''')

class delete_subjects(View):
    def get(self,request,id):
     obj1=subject_model.objects.get(id=id)
     obj1.delete()
     return HttpResponse('''<script>alert("deleted successfully");window.location="/subject"</script>''')





class assign_subject (View):
    def get(self,request):
        obj1=departrment_model.objects.all()
        obj2=staff_model.objects.all()
        obj3=subject_model.objects.all()

        return render(request,'hod/add_subject.html',{'obj1':obj1, 'obj2':obj2, 'obj3':obj3})

    

class Change_password(View):
    def get(self,request):
        return render(request,'hod/changepassword.html')   
    

class Hoddash(View):
    def get(self,request):
        return render(request,'hod/hoddash.html')   
    


class Manage_subject_allocated(View):
    def get(self,request):
        obj1=subject_model.objects.all()
        return render(request,'hod/manage_subject_allocated.html',{'obj1':obj1})   
    

class Notification(View):
    def get(self,request):
        return render(request,'hod/manage-niotification.html')   
    


class View_attendence_marked(View):
    def get(self,request):
        return render(request,'hod/view_attendence_marked.html')   
    

class View_profile(View):
    def get(self,request):
        return render(request,'hod/view-profile.html')   
    


class subject(View):
    def get(self,request):
        return render(request,'hod/subject.html')  

class view_staff(View):
    def get(self,request):
        obj=staff_model.objects.all()
        return render(request,'hod/view_staff.html',{'obj':obj})   
     

    

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



