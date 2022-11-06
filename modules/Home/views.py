import imp
from multiprocessing import get_context
from unittest import result
from django.shortcuts import render
from django.views.generic import ListView
from .models import homeTable
from django.http import JsonResponse
import json

from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from modules.Home.serializers import HomeSerializer
from rest_framework import viewsets





###  API View  ####


@api_view(['GET', 'POST'])
def getAllData(request):
    """
    List all Orders
    """
    if request.method == 'GET':
        allData = homeTable.objects.all()
        serializer = HomeSerializer(allData, many=True)
        return Response(serializer.data)





# Create your views here.
@csrf_exempt
def home(request):
    data = request.POST.getlist('data[]')
    allobjects2 = homeTable.objects.all()
    data="Hello"
    print(allobjects2)
    return render(request, 'home.html', {"allobjects2":allobjects2})

@csrf_exempt
def homeTab2(request):
    data = request.POST.getlist('data[]')
    print("data>>>",data)
    allobjects = homeTable.objects.all().filter(name__in=data)
    # allobjects2 = homeTable.objects.all()
    # print(allobjects)
    return render(request, 'home.html', {"allobjects":allobjects})


# class HomeView(ListView):
#     model = homeTable
#     template_name = 'home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["qs_json"] =  json.dumps(list(homeTable.objects.values()))
#         return context


def fetch_data(request,key):
    queryset = homeTable.objects.filter(name__contains=key)
    result = list(queryset.values("name"))
    return JsonResponse(result,safe=False)




