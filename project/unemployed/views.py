from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from .models import Unemployed
import json
import datetime

@csrf_exempt
def new(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        unemployed = Unemployed()
        unemployed.name = json_data['name']
        unemployed.dateOfBirth = datetime.datetime.strptime(json_data['dateOfBirth'], "%Y-%m-%d").date()
        unemployed.address = json_data['address']
        unemployed.email = json_data['email']
        unemployed.phoneNumber = json_data['phoneNumber']
        unemployed.cv = json_data['cv']
        unemployed.itmDocuments = json_data['itmDocuments']

        unemployed.save()
        return JsonResponse({'unemployedId': unemployed.id})
    else:
        return JsonResponse(['get'], safe=False)