from django.http import JsonResponse


def lets(request):
    return JsonResponse({'status':'accessed'})