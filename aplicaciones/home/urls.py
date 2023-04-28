from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dash/', Home.as_view(), name='home'),    
    path('login/',auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', MyPasswordChangeView.as_view(), name='pass_change'),
    path('change-password/done/', MyPasswordResetDoneView.as_view(), name='pass_change_done'),
]