from django.urls import path
from frontend import views

urlpatterns = [
    path('', views.homei, name="home"),
    path('discategory/<itemcatg>', views.discategory, name="discategory"),
    path('prosingle/<int:dataid>', views.prosingle, name="prosingle"),
    path('login1/', views.login1, name="login1"),
    path('customer/', views.customer, name="customer"),
    path('customerlogin/', views.customerlogin, name="customerlogin"),
    path('contact1', views.contact1, name="contact1"),
    path('contacte/', views.contacte, name="contacte"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
    path('check/',views.check, name="check"),
    path('boo/', views.boo, name="boo")

]