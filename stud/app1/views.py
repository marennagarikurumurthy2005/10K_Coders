from django.shortcuts import render,get_object_or_404
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Users,Students
from .seializer import userSerializer,studentSerializer
from .passwords import Passdecrypt,Passencrypt

# Create your views here.
@csrf_exempt
def register(request):
    data_comming = json.loads(request.body)
    data_comming['password']=Passencrypt(data_comming['password'])
    data_comming['repassword']=Passdecrypt(data_comming['repassword'],data_comming['password'])
    if data_comming['repassword']:
        data_comming['repassword']=data_comming['password']
        serilized_data = userSerializer(data=data_comming)
        print(serilized_data)
        if serilized_data.is_valid():
            serilized_data.save()
            return JsonResponse({'status':"Registered Successfully"})
        return JsonResponse(serilized_data.errors)
    return JsonResponse({'status':"invalid password match"})


@csrf_exempt
def login(request):
    data_comming = json.loads(request.body)
    user=data_comming['username']
    password=data_comming['password']
    extract_user=Users.objects.get(username=user)
    db_password=extract_user.password

    if Passdecrypt(password,db_password):
        response = JsonResponse({'status':'login success'})
        response.set_cookie(
            key='permission',
            value=True,
            max_age=60*5
        )
        request.session['username']="Murthy"
        return response

@csrf_exempt
def logout(request):
    response=JsonResponse({'status':'logout successful'})
    response.delete_cookie('permission')
    return response
    pass


@csrf_exempt
def add_student(request):
    if bool(request.COOKIES.get('permission')):
        response=json.loads(request.body)
        adding=studentSerializer(data=response)
        if adding.is_valid():
            adding.save()
            return JsonResponse({'status':'student added'})
        return JsonResponse({'status':adding.errors})
    return JsonResponse({'note':'login cheyra Hooka'})

@csrf_exempt 
def delete_student(request,id):
    if bool(request.COOKIES.get('permission')):
        data=get_object_or_404(Students,id=id)
        data.delete()
        return JsonResponse({'status':'data deleted'})

    return JsonResponse({'note':'login cheyra Hooka'})

@csrf_exempt
def update_student(request,id):
    if bool(request.COOKIES.get('permission')):
        raw_data=json.loads(request.body)
        data=get_object_or_404(Students,id=id)
        serializer_data=studentSerializer(instance=data,data=raw_data,partial=True)
        if serializer_data.is_valid():
            serializer_data.save()
            return JsonResponse({'status':"update succes"})
        return JsonResponse(serializer_data.errors)
    return JsonResponse({'note':'login cheyra Hooka'})

    pass


def home(request):
    if bool(request.COOKIES.get('permission')):
        datas=Students.objects.all()
        serializer_data=studentSerializer(datas,many=True).data
        return JsonResponse(serializer_data,safe=False)
    return JsonResponse({'note':'login cheyra Hooka'})





