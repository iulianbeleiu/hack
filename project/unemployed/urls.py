from django.urls import path, include
from . import views
from unemployed.views import new

urlpatterns = [
    path('new', views.new, name='new'),
    # path('<int:id>', detail, name='detail'),
]