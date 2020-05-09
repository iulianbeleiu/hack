from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Company, Revenue, Product


@csrf_exempt
def new(request):
    try:
        if request.method == 'POST':
            json_data = json.loads(request.body)
            company = Company()
            company.name = json_data['name']
            company.address = json_data['address']
            company.email = json_data['email']
            company.phoneNumber = json_data['phoneNumber']
            company.fiscalData = json_data['fiscalData']
            company.activityDomain = json_data['activityDomain']

            company_revenue = json_data['revenue']
            revenues = Revenue.objects.all()
            revenue_id = None
            for revenue in revenues:
                if revenue.intervalMax >= int(company_revenue) >= revenue.intervalMin:
                    revenue_id = revenue

            if revenue_id:
                company.revenue = revenue_id
            else:
                company.revenue = Revenue()
            company.save()
            return JsonResponse({'companyId': company.id})
        else:
            return JsonResponse(['get'], safe=False)
    except(Exception):
        return JsonResponse({'message': 'Internal Server Error'}, status=500)


def detail(request, id):
    try:
        company = Company.objects.get(pk=id)
        return JsonResponse({
            'name': company.name,
            'address': company.address,
            'email': company.email,
            'phoneNumber': company.phoneNumber,
            'fiscalData': company.fiscalData,
            'activityDomain': company.activityDomain,
            'revenue': company.revenue.percent,
        }, safe=False)
    except:
        return JsonResponse({}, status=404)


def company_products(request, id):
    try:
        company_products = Product.objects.all().filter(company=id)
        products = []
        for product in company_products:
            products.append({
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'company_id': product.company.id,
            })

        if company_products:
            return JsonResponse(products, safe=False)
        else:
            return JsonResponse({}, status=404)
    except:
        return JsonResponse({}, status=404)


def company_product(request, company_id, product_id):
    try:
        company_product = Product.objects.get(company=company_id, pk=product_id)

        if company_product:
            product = {
                'id': company_product.id,
                'name': company_product.name,
                'description': company_product.description,
                'price': company_product.price,
                'company_id': company_product.company.id,
            }
            return JsonResponse(product, safe=False)
        else:
            return JsonResponse({}, status=404)
    except:
        return JsonResponse({}, status=404)