from django.contrib import admin
from django.urls import path
from app1 import views


urlpatterns = [
    path('index/', views.index, name="index"),
    path('addadmin/', views.adminpage, name="addadmin"),
    path('admin/', views.admin, name="admin"),
    path('diaplayadmin/', views.displayadmin, name="displayadmin"),
    path('editadmin/<int:dataid>/', views.editadmin, name="editadmin"),
    path('updateadmin/<int:dataid>/', views.updateadmin, name="updateadmin"),
    path('deleteadmin/<int:dataid>/', views.deleteadmin, name="deleteadmin"),

    path('addcategory/', views.addcategory, name="addcategory"),
    path('category/', views.category, name="category"),
    path('diaplaycategory/', views.displaycategory, name="displaycategory"),
    path('editcategory/<int:dataid>/', views.editcategory, name="editcategory"),
    path('updatecategory/<int:dataid>/', views.updatecategory, name="updatecategory"),
    path('deletecategory/<int:dataid>/', views.deletecategory, name="deletecategory"),

    path('addproduct/', views.addproduct, name="addproduct"),
    path('product/', views.product, name="product"),
    path('diaplayproduct/', views.displayproduct, name="displayproduct"),
    path('editproduct/<int:dataid>/', views.editproduct, name="editproduct"),
    path('updateproduct/<int:dataid>/', views.updateproduct, name="updateproduct"),
    path('deleteproduct/<int:dataid>/', views.deleteproduct, name="deleteproduct"),

    path('logina/', views.logina, name="logina"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),

    path('customers/', views.customers, name="customers"),
    path('deletecustomer/<int:dataid>/', views.deletecustomer, name="deletecustomer")


]
