from pingponghit.models import Pingponghit
from django.shortcuts import render
from rest_framework import generics, serializers
import json
from datetime import datetime
import pandas as pd
from dateutil.parser import parse 
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy import *
from scipy.signal import *
# Create your views here.
from pingponghit import models
from .serializers import PingponghitSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt



# class ListPingponghit(generics.ListCreateAPIView):
@csrf_exempt
def pingponghit_list(request):
    if request.method == 'GET':
        pingponghit = Pingponghit.objects.all()
        serializer = PingponghitSerializer(pingponghit, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PingponghitSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def pingponghit_detail(request, pk):
    try:
        pingponghit = Pingponghit.objects.get(pk=pk)
    except Pingponghit.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PingponghitSerializer(pingponghit)
        title = serializer.data['title']
        print(title)
        # print (res)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        #append data to list
        xaccele = []
        yaccele = []
        zaccele = []
        xgyro = []
        ygyro = []
        zgyro = []
        avg = 0
        listdata = []

        data = JSONParser().parse(request)
        serializer = PingponghitSerializer(pingponghit, data=data)

        if serializer.is_valid():
            sensor = json.loads(serializer.data['data'])
            for a in sensor['accelerometer'] :
                xaccele.append(a[0])
                yaccele.append(a[1])
                zaccele.append(a[2])
            
            for g in sensor['gyroscope']:
                xgyro .append(g[0])
                ygyro.append(g[1])
                zgyro.append(g[2])
            

            if serializer.data['title'] == 'Forehand' :
                #cal pingponghit accele
                #cal by xaccele
                arrayXaccele = np.array(xaccele)
                peaks, _ = find_peaks(arrayXaccele, distance=150)
                np.diff(peaks)

                #cal by yaccele
                arrayYaccele = np.array(yaccele)
                peaks, _ = find_peaks(arrayYaccele, distance=150)
                np.diff(peaks)
                
                #cal by zaccele
                arrayZaccele = np.array(zaccele)
                peaks, _ = find_peaks(arrayZaccele, distance=150)
                np.diff(peaks)
                
                #cal pingponghit gyro
                #cal by xgyro
                arrayXgyro = np.array(xgyro)
                peaks, _ = find_peaks(arrayXgyro,height=2.5, distance=150)
                np.diff(peaks)
                
                

                arrayYgyro = np.array(xgyro)
                peaks, _ = find_peaks(arrayYgyro,height=2.5, distance=150)
                np.diff(peaks)
                
                

                arrayZgyro = np.array(xgyro)
                peaks, _ = find_peaks(arrayZgyro,height=2.5, distance=150)
                np.diff(peaks)
                
                listdata.append(len(arrayXgyro[peaks]))
                listdata.append(len(arrayYgyro[peaks]))
                listdata.append(len(arrayZgyro[peaks]))
                avglist = sum(listdata)/len(listdata)
                avg = int(avglist)
            else :
                #cal pingponghit accele
                #cal by xaccele
                arrayXaccele = np.array(xaccele)
                peaks, _ = find_peaks(arrayXaccele, distance=150)
                np.diff(peaks)

                #cal by yaccele
                arrayYaccele = np.array(yaccele)
                peaks, _ = find_peaks(arrayYaccele, distance=150)
                np.diff(peaks)
                
                #cal by zaccele
                arrayZaccele = np.array(zaccele)
                peaks, _ = find_peaks(arrayZaccele, distance=150)
                np.diff(peaks)
                
                #cal pingponghit gyro
                #cal by xgyro
                arrayXgyro = np.array(xgyro)
                peaks, _ = find_peaks(arrayXgyro,height=2.5, distance=150)
                np.diff(peaks)
                
                

                arrayYgyro = np.array(xgyro)
                peaks, _ = find_peaks(arrayYgyro,height=2.5, distance=150)
                np.diff(peaks)
                
                

                arrayZgyro = np.array(xgyro)
                peaks, _ = find_peaks(arrayZgyro,height=2.5, distance=150)
                np.diff(peaks)
                
                listdata.append(len(arrayXgyro[peaks]))
                listdata.append(len(arrayYgyro[peaks]))
                listdata.append(len(arrayZgyro[peaks]))
                avglist = sum(listdata)/len(listdata)
                avg = int(avglist)

            
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        pingponghit.delete()
        return HttpResponse(status=204)
