import imp
from django.urls import path
from modules.Home.views import home,fetch_data,homeTab2,getAllData

# from modules.Home.views import HomeView

urlpatterns = [
    path('',home,name='home'),
    path('api/getDatasdkfn', getAllData),
    path('homeTab2/',homeTab2,name='homeTab2'),
    path('fetch_data/<str:key>/',fetch_data,name='fetch_data'),
]

