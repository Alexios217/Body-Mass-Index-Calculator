from django.http import JsonResponse
from .utils.bmi_script import calculate_bmi

def bmi_view(request):
    """Handle BMI calculation requests."""
    if request.method == "GET":
        try:
            weight = float(request.GET.get("weight", 0))
            height = float(request.GET.get("height", 1))  # Prevent division by zero
            age = int(request.GET.get("age", 0))

            result = calculate_bmi(weight, height, age)  # Use the imported function

            return JsonResponse(result)
        except ValueError:
            return JsonResponse({"error": "Invalid input. Please provide numeric values."}, status=400)
    
    return JsonResponse({"error": "Invalid request method"}, status=405)
