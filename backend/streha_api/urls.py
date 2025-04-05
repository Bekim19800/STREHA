from django.http import JsonResponse
from django.urls import path

def listings(request):
    try:
        data = [
            {"id": 1, "title": "Cozy Apartment in Tirana"},
            {"id": 2, "title": "Modern Villa in Durrës"}
        ]
        return JsonResponse(data, safe=False)
    except Exception as e:
        # Return the error message in the response for debugging
        return JsonResponse({"error": str(e)}, status=500)

urlpatterns = [
    path("listings/", listings),
]
