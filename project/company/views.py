from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
from django.core import serializers
import json
from .models import Company



# Create your views here.
@csrf_exempt
def new(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        company = Company()
        company.name = json_data['name']
        company.address = json_data['address']
        company.email = json_data['email']
        company.phoneNumber = json_data['phoneNumber']
        company.fiscalData = json_data['fiscalData']
        company.activityDomain = json_data['activityDomain']
        company.revenueId = 1
        company.save()
        return JsonResponse({'companyId': company.id})
    else:
        return JsonResponse(['get'], safe=False)


def detail(request, id):
    company = get_object_or_404(Company, pk=id)
    return JsonResponse({
        'name': company.name,
        'address': company.address,
        'email': company.email,
        'phoneNumber': company.phoneNumber,
        'fiscalData': company.fiscalData,
        'activityDomain': company.activityDomain,
        'revenue': company.revenueId,
    }, safe=False)