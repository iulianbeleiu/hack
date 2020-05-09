from django.urls import path, include
from . import views
from company.views import new, detail

urlpatterns = [
    path('new', views.new, name='new'),
    path('<int:id>', detail, name='detail'),
]