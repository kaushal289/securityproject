from django.urls import path
from product import views 
urlpatterns = [
    path('product_create',views.product_create),
    path('deleteproduct/<int:p_id>',views.deleteproduct),
    path('editproduct/<int:p_id>',views.editproduct),
    path('productupdate/<int:p_id>',views.productupdate),
]
