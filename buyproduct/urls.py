from django.urls import path
from buyproduct import views 
urlpatterns = [
    path('buypage/<int:p_id>',views.buypage, name='buypage'),
    path('bill_create',views.bill_create,name="bill_create"),
    path('yourproduct',views.yourproduct, name="yourproduct"),
    path('updatedelete/<int:e_id>',views.updatedelete,name="updatedelete"),
]
