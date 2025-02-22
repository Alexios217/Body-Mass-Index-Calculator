# Body-Mass-Index-Calculator
The BMI Calculator Web App is a Django-based application that allows users to input their height, weight, and other details to calculate their Body Mass Index (BMI). 

# **BMI Calculator Web App Documentation**

## **Introduction**
The **BMI Calculator Web App** is a Django-based application that allows users to input their height, weight, and other details to calculate their Body Mass Index (BMI). This document covers **Steps 1-9** of the development process, detailing how the app is structured and implemented.

---

## **Step 1: Setting Up the Django Project**

To begin, install Django if you haven't already:
```bash
pip install django
```
Create a new Django project:
```bash
django-admin startproject bmi_project
```
Navigate into the project directory:
```bash
cd bmi_project
```
Start a new app for the BMI calculator:
```bash
python manage.py startapp bmi_calculator
```
Register the app in `settings.py`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bmi_calculator',
]
```

---

## **Step 2: Creating the BMI Model**

Define the BMI calculation model in `bmi_calculator/models.py`:
```python
from django.db import models

class BMICalculation(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    height = models.FloatField()
    weight = models.FloatField()
    bmi = models.FloatField()
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
```
Apply migrations:
```bash
python manage.py makemigrations bmi_calculator
python manage.py migrate
```

---

## **Step 3: Setting Up URLs**

In `bmi_calculator/urls.py`, define the URL patterns:
```python
from django.urls import path
from .views import bmi_form, calculate_bmi

urlpatterns = [
    path('', bmi_form, name='bmi_form'),
    path('calculate/', calculate_bmi, name='calculate_bmi'),
]
```
Include these URLs in `bmi_project/urls.py`:
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bmi/', include('bmi_calculator.urls')),
]
```

---

## **Step 4: Creating the BMI Form**

Define an HTML form in `templates/bmi_calculator/form.html`:
```html
<form method="post" action="{% url 'calculate_bmi' %}">
    {% csrf_token %}
    <label for="name">Name:</label>
    <input type="text" name="name" required>
    <label for="age">Age:</label>
    <input type="number" name="age" required>
    <label for="gender">Gender:</label>
    <select name="gender">
        <option value="Male">Male</option>
        <option value="Female">Female</option>
    </select>
    <label for="height">Height (m):</label>
    <input type="text" name="height" required>
    <label for="weight">Weight (kg):</label>
    <input type="text" name="weight" required>
    <button type="submit">Calculate</button>
</form>
```

---

## **Step 5: Implementing the BMI Calculation Logic**

In `bmi_calculator/views.py`, process the form and calculate BMI:
```python
from django.shortcuts import render
from .models import BMICalculation

def bmi_form(request):
    return render(request, 'bmi_calculator/form.html')

def calculate_bmi(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = int(request.POST['age'])
        gender = request.POST['gender']
        height = float(request.POST['height'])
        weight = float(request.POST['weight'])
        bmi = weight / (height ** 2)
        
        if bmi < 20:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal Weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        BMICalculation.objects.create(
            name=name, age=age, gender=gender, height=height, weight=weight, bmi=bmi, category=category
        )
        
        return render(request, 'bmi_calculator/result.html', {'bmi': bmi, 'category': category})
```

---

## **Step 6: Displaying the Results**

Create `templates/bmi_calculator/result.html`:
```html
<h2>Your BMI Result</h2>
<p>Your BMI: {{ bmi|floatformat:2 }}</p>
<p>Category: {{ category }}</p>
<a href="{% url 'bmi_form' %}">Calculate Again</a>
```

---

## **Step 7: Testing the Application**

Run the development server:
```bash
python manage.py runserver
```
Access the form at:
```
http://127.0.0.1:8000/bmi/
```
Enter details and calculate BMI to see results.

---

## **Step 8: Storing Data in the Database**

The `BMICalculation` model automatically stores each entry in the database. To view stored data:
```bash
python manage.py shell
```
Then, enter:
```python
from bmi_calculator.models import BMICalculation
BMICalculation.objects.all()
```

---

## **Step 9: Admin Panel Integration**

To manage BMI records via Django Admin, register the model in `bmi_calculator/admin.py`:
```python
from django.contrib import admin
from .models import BMICalculation

admin.site.register(BMICalculation)
```
Create a superuser:
```bash
python manage.py createsuperuser
```
Then, log in at:
```
http://127.0.0.1:8000/admin/
```

---

## **Conclusion**
Steps 1-9 covered setting up the Django project, implementing the BMI calculator, storing data in the database, and integrating it with the Django Admin panel. Future steps will include enhancing the UI, adding analytics, and implementing a dashboard.

---

### **Next Steps**
Would you like to move forward with **data visualization** and **advanced analytics** next? 🚀

