from django.urls import path,include
from .views import change_pwview,loginview,logoutview,registerview,homeview
from django.contrib.auth import views as auth_view



urlpatterns = [
    path('home/', homeview, name='home'),
    path('home/login/', loginview, name='login'),
    path('home/logout/', logoutview, name='logout'),
    path('home/login/register/', registerview, name='register'),
    path('home/change_pw/', change_pwview, name='changepw'),
    path('login/password_reset/', auth_view.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_view.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_view.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
