from django.http import JsonResponse
from django.urls import path

def listings(request):
    data = [
        {"id": 1, "title": "Cozy Apartment in Tirana"},
        {"id": 2, "title": "Modern Villa in Durrës"}
    ]
    return JsonResponse(data, safe=False)

urlpatterns = [
    path("listings/", listings),
]
