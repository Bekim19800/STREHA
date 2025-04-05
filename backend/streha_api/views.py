from django.http import JsonResponse

def listings(request):
    data = [
        {"id": 1, "title": "Cozy Apartment in Tirana"},
        {"id": 2, "title": "Modern Villa in Durrës"}
    ]
    return JsonResponse(data, safe=False)
