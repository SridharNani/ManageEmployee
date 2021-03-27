from django.shortcuts import render
from rest_framework.generics import GenericAPIView, CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from .serializers import UserSerializer, LoginSerializer, EmplyeeSerializer
from rest_framework.response import Response
from rest_framework import status

from .models import Manager, Employee
from django.http import HttpResponse

# Create your views here.


class RegisterAPI(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):

        ls = LoginSerializer(data=request.data)
        if ls.is_valid():
            try:
                Manager.objects.get(email=ls.validated_data['email'], password=ls.validated_data['password'])
                request.session['email'] = ls.validated_data['email']
                data = {"create":"http://127.0.0.1:8000/app/create","read":"http://127.0.0.1:8000/app/view_all"}
                return HttpResponse(data)
            except Manager.DoesNotExist:
                return Response({'message': "Invalid username and password"})

        return Response(ls.errors)


class ManagerApi(CreateAPIView):
    serializer_class = EmplyeeSerializer
    queryset = Employee.objects.all()

class EmployeeViewAll(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmplyeeSerializer


class EmployeeDelete(DestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class = EmplyeeSerializer
#
#
class EmployeeUpdate(UpdateAPIView):
    queryset=Employee.objects.all()
    serializer_class = EmplyeeSerializer


