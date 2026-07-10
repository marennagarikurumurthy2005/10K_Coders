from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import cloudinary
import cloudinary.uploader
from .models import Surya_table
from .serializer import Suryaserializer
# Create your views here.

@method_decorator(csrf_exempt,name='dispatch')
class CreateView(View):
    def get(self,req):
        return JsonResponse({'status':"this is for get method"})
    def post(self,req):
        image=req.FILES.get('image')
        image_data = cloudinary.uploader.upload(image,folder='samples')
        image_url = image_data.get('secure_url')

        data={
            'name':req.POST.get('name'),
            'age':req.POST.get('age'),
            'image':image_url
        }
        ser_data = Suryaserializer(data=data)
        if ser_data.is_valid():
            ser_data.save()
            return JsonResponse({'status':'data saved successfully'})
        
        return JsonResponse(ser_data.errors)
    
    def delete(self,req):
        return JsonResponse({'status':"this is for delete method"})

