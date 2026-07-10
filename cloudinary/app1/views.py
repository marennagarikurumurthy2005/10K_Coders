from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@method_decorator(csrf_exempt,name='dispatch')
class CreateView(View):
    def get(self,req):
        return JsonResponse({'status':"this is for get method"})
    def post(self,req):
        return JsonResponse({'status':"this is for post method"})
    def delete(self,req):
        return JsonResponse({'status':"this is for delete method"})

