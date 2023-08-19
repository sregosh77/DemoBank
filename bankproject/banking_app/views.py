from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect


def home(request):
    return render(request, 'home.html')


def dashboard(request):
    return render(request, 'dashboard.html')

def thrissur_page(request):
    return render(request, 'thrissur.html')

def kochi_page(request):
    return render(request, 'kochi.html')

def kannur_page(request):
    return render(request, 'kannur.html')

def palakkad_page(request):
    return render(request, 'palakkad.html')

def malappuram_page(request):
    return render(request, 'malappuram.html')

def form_page(request):
    districts = {
        'thrissur': ['VARANDARAPPILLY', 'CHALAKUDY'],
        'kochi': ['ALUVA', 'PALARIVATTOM'],
        'kannur': ['TALIPARAMBA', 'PANJARAMUKK'],
        'palakkad': ['PATTAMBI', 'SHORNUR'],
        'malappuram': ['PONNANI', 'TIRUR'],
    }

    selected_district = request.POST.get('district','thrissur')
    selected_branches = districts.get(selected_district, [])

    if request.method == 'POST':
        # Process the form data here
        messages.success(request, 'Application accepted')

    return render(request, 'form.html', {'districts': districts, 'selected_district': selected_district, 'selected_branches': selected_branches})