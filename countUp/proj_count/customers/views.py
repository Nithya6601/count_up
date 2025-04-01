from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import Customer
from django.http import JsonResponse

# Create your views here.

class MainView(TemplateView):
    template_name = 'customers/main.html'

class CustomerNumJsonView(View):
    def get(self, *agrs, **kwargs):
        customer_count = Customer.objects.filter(active=True).count()
        return JsonResponse({'customer_count': customer_count})

