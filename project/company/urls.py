from django.urls import path, include
from . import views
from company.views import new, detail, company_products, company_product

urlpatterns = [
    path('new', views.new, name='new'),
    path('<int:id>', detail, name='detail'),
    path('<int:id>/products', company_products, name='company_products'),
    path('<int:company_id>/product/<int:product_id>', company_product, name='company_product'),
]