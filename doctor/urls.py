"""
URL configuration for doctor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from doctor_app import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.Register.as_view(),name='register'),
    # path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    # path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'),
    # path('verifytoken/',TokenVerifyView.as_view(),name='token_verify'),
    path('login/',views.Login.as_view(),name='login'),
    path('userprofile/',views.UserProfileView.as_view(),name = 'profile'),
    path('doctorlist/',views.UserDoctorView.as_view(),name = 'doctorlist'),
    path('userlist/',views.AdminView.as_view(),name='userlist'),
    path('userlist/<int:pk>/',views.AdminView.as_view(),name='userlist'),





]
