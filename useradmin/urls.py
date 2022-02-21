from django.urls import path
from useradmin import views 
urlpatterns = [
    path('admindash', views.admindash),
    path('adminproduct', views.adminproduct),
    path('customer_delete/<int:p_id>',views.customer_delete),
    path('billing',views.billing),
    path('updatecomplete/<int:e_id>',views.updatecomplete),
    path('deletebill/<int:d_id>',views.deletebill),
    path('adduser',views.adduser,name='adduser'),
    path('userinfo',views.userinfo,name='viewuser'),
    path('edituser/<int:p_id>',views.edituser),
    path('updateuser/<int:p_id>',views.updateuser),
    path('deleteuser/<int:p_id>',views.deleteuser),
]