from django.contrib import messages

# Create your views here.

from django.contrib.auth import authenticate, login
from django.urls import reverse

from rest_framework import permissions, generics
from .serializer import RegisterSerializer,CustomUserSerializer,CustomTokenObtainPairSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
import requests
from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView

from django.shortcuts import redirect


class Register(APIView):
    def post(self,request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        user = serializer.create(serializer.validated_data)
        refresh = RefreshToken.for_user(user)
        user = CustomUserSerializer(user)
        data = {
            "refresh":str(refresh),
            "access":str(refresh.access_token),
            "user":user.data
        }
        return Response(data,status=status.HTTP_201_CREATED)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class VerifyUser(APIView):
    permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = (TokenAuthentication,)

    def get(self,request):
        user = request.user
        print("######################################",user.id)
        user = CustomUserSerializer(user)
        data = {"user":user.data}
        print("############3444444444444444",data)
        return Response(data,status=status.HTTP_200_OK)

def register(request):
    response = requests.get('http://127.0.0.1:8000/user/RegisterAPI/')
    data = response.json()
    return render(request,'register.html',{'data':data})




def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page or any desired URL
            return redirect(reverse('list'))
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')

    # If the request method is not POST or login failed, render the login form.
    return render(request, 'login.html')



