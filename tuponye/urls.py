from django.contrib import admin
from django.urls import path
from tuponye import views

urlpatterns = [
    path("",views.index, name = 'home'),
    path("index",views.index, name = 'index'),
    path("about",views.about,name = 'about'),
    path("adminlogin", views.adminlogin, name="adminlogin"),
    path("admin_home", views.admin_home, name="admin_home"),
    path("Logout",views.Logout,name = "Logout"),
    path("add_doctor",views.add_doctor,name = "add_doctor"),
    path("view_doctor",views.view_doctor,name = "view_doctor"),
    path("Delete_Doctor",views.Delete_Doctor,name = "Delete_Doctor"),
    path("edit_doctor",views.edit_doctor,name = "edit_doctor"),
    path("add_patient",views.add_patient,name = "add_patient"),
    path("view_patient",views.view_patient,name = 'view_patient'),
    path("Delete_Patient",views.Delete_Patient,name = 'Delete_Patient'),
    path("edit_patient",views.edit_patient,name = 'edit_patient'),
    path("add_appointment",views.add_appointment,name = 'add_appointment'),
    path("view_appointment",views.view_appointment,name = 'view_appointment'),
    path("Delete_Appointment",views.Delete_Appointment,name = 'Delete_Appointment'),
    path("unread_queries",views.unread_queries,name = 'unread_queries'),
    path("read_queries",views.read_queries,name = 'read_queries'),
    path("view_queries",views.view_queries,name = 'view_queries'),
    path("contact",views.contact,name = 'contact'),
    

    ]