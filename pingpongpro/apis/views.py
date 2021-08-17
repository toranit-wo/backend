from pingponghit.models import Pingponghit,Totalhit
from .serializers import PingponghitSerializer,TotalhitSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


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
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PingponghitSerializer(pingponghit, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        pingponghit.delete()
        return HttpResponse(status=204)

@csrf_exempt
def totalhit_list(request):
    if request.method == 'GET':
        totalhit = Totalhit.objects.all()
        serializer = TotalhitSerializer(totalhit, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TotalhitSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def totalhit_detail(request, pk):
    try:
        totalhit = Totalhit.objects.get(pk=pk)
    except Totalhit.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TotalhitSerializer(totalhit)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TotalhitSerializer(totalhit, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        totalhit.delete()
        return HttpResponse(status=204)