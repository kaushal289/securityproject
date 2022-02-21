from django.urls import path
from buyproduct import views 
urlpatterns = [
    path('buypage/<int:p_id>',views.buypage),
    path('bill_create',views.bill_create),
    path('yourproduct',views.yourproduct),
    path('updatedelete/<int:e_id>',views.updatedelete),
]
