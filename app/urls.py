from django.urls import path

# from app import views
from django.views.decorators.csrf import csrf_exempt

from app import views
from app.views import RegisterAPI, LoginAPI, ManagerApi, EmployeeViewAll, EmployeeDelete, EmployeeUpdate

urlpatterns=[
    path('register/',RegisterAPI.as_view(),name='register'),
    path('login/',LoginAPI.as_view(),name='register'),
    path('create/',ManagerApi.as_view(),name='manager'),
    path('view_all/',EmployeeViewAll.as_view()),
    # path('view_all/',EmployeeRetrieve.as_view()),
    path('delete_one/<pk>',EmployeeDelete.as_view()),
    path('update/<pk>',EmployeeUpdate.as_view()),
    # path('logout/',Logout.as_view())
         ]