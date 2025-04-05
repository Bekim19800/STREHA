from django.http import JsonResponse, HttpResponse

def listings(request):
    data = [
        {"id": 1, "title": "Cozy Apartment in Tirana"},
        {"id": 2, "title": "Modern Villa in Durrës"}
    ]
    return JsonResponse(data, safe=False)

def index(request):
    return HttpResponse("Backend up and running.")
