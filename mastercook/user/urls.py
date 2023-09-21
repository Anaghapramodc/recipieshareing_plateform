from . import views
from django.urls import path

from .views import Register,MyTokenObtainPairView,VerifyUser

urlpatterns = [
    path('RegisterAPI/', Register.as_view(), name='register'),
    path('verifyuser/',VerifyUser.as_view()),
    path('loginAPI/',MyTokenObtainPairView.as_view(), name='login'),
    path('register/',views.register,name='Register'),
    path('login/', views.user_login, name='Login'),

]