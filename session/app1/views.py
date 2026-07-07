from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def create_session(request):
    data = json.loads(request.body)
    if data['username']=="murthy123" and data['password']=='murthy@123':
        request.session['username']='Murthy'
        response = JsonResponse({'status':"valid credits"})
        return response
    return JsonResponse({'status':'invalid credits'})

@csrf_exempt
def get_session(request):
    data = request.session['username']
    if request.session:
        request.session.flush()
        return JsonResponse({'status':'session deleted'})
    return JsonResponse({'status':'cant find session'})