from django.http import JsonResponse

def calculate_bmi(request):
    try:
        weight = float(request.GET.get('weight'))
        height = float(request.GET.get('height'))
        age = int(request.GET.get('age'))

        if weight <= 0 or height <= 0 or age <= 0:
            return JsonResponse({'error': 'Values must be greater than zero'})

        bmi = weight / (height ** 2)

        # Determine age category
        if age <= 12:
            age_category = "child"
        elif age <= 17:
            age_category = "teenager"
        elif age <= 59:
            age_category = "adult"
        else:
            age_category = "elderly person"

        # Determine weight category
        if bmi < 20:
            weight_category = "underweight"
        elif bmi < 25:
            weight_category = "normal weight"
        elif bmi < 30:
            weight_category = "low-risk obese"
        elif bmi < 35:
            weight_category = "high-risk obese"
        else:
            weight_category = "severely obese"

        return JsonResponse({
            'bmi': round(bmi, 2),
            'weight_category': weight_category,
            'age_category': age_category
        })

    except (TypeError, ValueError):
        return JsonResponse({'error': 'Invalid input. Please enter numbers only.'})
