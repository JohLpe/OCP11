from email import message
from pyexpat.errors import messages
from django.urls import path, reverse_lazy
from django.contrib.auth.views import PasswordChangeView

from . import views

urlpatterns = [
    path('', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('account/', views.view_account, name='viewaccount'),
]
