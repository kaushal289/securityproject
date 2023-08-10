from django.urls import path
from customer import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.dashboard,name="dashboard"),
    path('register', views.register,name="register"),
    path('login',views.login_redirect,name="login"),
    path('profile',views.profile,name="profile"),
    path('update_password/<int:p_id>',views.update_password,name="update_password"),
    path('logout',views.logout,name='logout'),
    path('customer_update/<int:p_id>', views.update,name='update'),
    
    path('password_reset/',
    auth_views.PasswordResetView.as_view(template_name='auth/password_reset_form.html'),
    name='password_reset'),
    path('password_reset/done/',
    auth_views.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'),
    name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'),
    name='password_reset_confirm'),
    path('reset/done/',
    auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'),
    name='password_reset_complete'),

]
