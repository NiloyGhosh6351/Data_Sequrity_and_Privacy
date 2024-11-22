from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Patient
from .query import query_patients_by_weight_range


def home(request):
    if request.user.is_authenticated:
        groups = [group.name for group in request.user.groups.all()]
        patients_data = []

        min_weight = request.GET.get('min_weight', None)
        max_weight = request.GET.get('max_weight', None)

        if min_weight and max_weight and ('H' in groups or 'R' in groups):
            # Convert to integers if needed
            min_weight = int(min_weight)
            max_weight = int(max_weight)
            patients = query_patients_by_weight_range(min_weight, max_weight)

            if 'R' in groups:
                patients = patients.exclude(first_name=None, last_name=None)
            return render(request, 'index.html', {'patients': patients_data})

        return render(request, 'index.html', {'error': 'You are not authorized to view this page'})
    return redirect("login")


def weight_range(request):
    # Example range values, you can modify this to get the range from the request
    min_weight = request.GET.get('min_weight', None)
    max_weight = request.GET.get('max_weight', None)

    if min_weight and max_weight:
        # Convert to integers if needed
        min_weight = int(min_weight)
        max_weight = int(max_weight)
        patients = query_patients_by_weight_range(min_weight, max_weight)
    else:
        # Return an empty queryset if no valid range is provided
        patients = Patient.objects.none()

    return render(request, 'index.html', {'patients': patients})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, 'login.html', {'error': 'Invalid Credentials'})
    if request.user.is_authenticated:
        return redirect("home")
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect("login")
