from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings

mail = settings.EMAIL_HOST_USER

# Create your views here.
# @csrf_exempt
# def create_session(request):
#     data = json.loads(request.body)
#     if data['username']=="murthy123" and data['password']=='murthy@123':
#         request.session['username']='Murthy'
#         response = JsonResponse({'status':"valid credits"})
#         return response
#     return JsonResponse({'status':'invalid credits'})

# @csrf_exempt
# def get_session(request):
#     data = request.session['username']
#     if request.session:
#         request.session.flush()
#         return JsonResponse({'status':'session deleted'})
#     return JsonResponse({'status':'cant find session'})

def welcome(req):
    send_mail(
    subject = "Test Email from Django",
    message = "Hello, this email is sent using Django.",
    from_email = 'marennagarikurumurthy2005@gmail.com@gmail.com',
    recipient_list = ["kurumurthy724@gmail.com"],
    fail_silently=True
    )
    return JsonResponse({'status':"Email Sent Successfully"})
