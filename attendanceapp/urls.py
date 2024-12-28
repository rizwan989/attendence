
from django.urls import include, path

from .views import *

urlpatterns = [
    path('', login_page.as_view(), name='login_page'),
    path('logout', logout.as_view()),

    # ////////////////////////////////////////  ADMIN /////////////////////////////////////////////////////

    path('addstaff', Add_staff.as_view(), name='addstaff'),

    path('adddept', Add_dept.as_view(), name='adddept'),

    path('addnotificaton', Add_notification.as_view(), name='addnotification'),

    path('addstudent', Add_student.as_view(), name='addstudent'),

    path('dashboard', Admin_dashboard.as_view(), name='dashboard'),

    path('editdept/<int:pk>', Edit_dept.as_view(), name='editstaff'),

    path('editstaff/<int:pk>', Edit_staff.as_view(), name='editstaff'),

    path('editstudent/<int:pk>', Edit_student.as_view(), name='editstudent'),

    path('managedept', Manage_department.as_view(), name='managedept'),

    path('managestaff', Manage_staff.as_view(), name='managestaff'),

    path('managestudent', Manage_student.as_view(), name='managestudent'),
    

    path('replycomplaints/<int:pk>/', Reply_complaints.as_view(), name='replycomplaints'),


    path('viewcomplaintssendreply', View_complaint_send_reply.as_view(), name='viewcomplaintsendreply'),

    path('managenotification', manage_notification.as_view(), name='managenot'),

    path('deletenot/<int:pk>', deletenotification.as_view(), name='deletenot'),

    path('deletedept/<int:pk>', deletedept.as_view(), name='deletedept'),

    path('deletestudent/<int:pk>', deletestudent.as_view(), name='deletestudent'),


    path('deletestaff/<int:pk>', deletestaff.as_view(), name='deletestaff'),



    

# //////////////////////////////////////////// hod//////////////////////////////


    path('approve', Approve_daily_leave.as_view(), name='approve'),

    path('chngepass', Change_password.as_view(), name='chngepass'),

    path('hoddash', Hoddash.as_view(), name='hoddash'),


    path('subjectallocated', Manage_subject_allocated.as_view(), name='subjectallocated'),

    path('notification', Notification.as_view(), name='notification'),

    path('subject', Manage_subjects.as_view(), name='subjects'),

    path('attendence', View_attendence_marked.as_view(), name='attendence'),

    path('profile', View_profile.as_view(), name='profile'),


#//////////////////////////////////////////////////////////////////////////////

    path('password', Change_password.as_view(), name='password'),

    path('staffandstudent', Deptwise_staffandstudent.as_view(), name='staffandstudent'),

    path('correctionrequest', Handle_correction_request.as_view(), name='correctionrequest'),

    path('teacherdash', Teacherdash.as_view(), name='teacherdash'),

    path('teacherlogin', Teacherlogin.as_view(), name='teacherlogin'),

    path('attendencemarked', View_attendence_marked.as_view(), name='attendencemarked'),

    path('notification', Notification.as_view(), name='notification'),

    path('subjectallocated', Subject_allocated.as_view(), name='subjectallocated'),

    path('profile', Viewandedit_profile.as_view(), name='profile'),


]