from django.shortcuts import render

# Create your views here.
def generative_agriculture(request):
    return render(request, 'AgricultureDetails/generative_agriculture.html')

def soil_practices(request):
    return render(request, 'AgricultureDetails/soil_practices.html')

def soil_effects(request):
    return render(request, 'AgricultureDetails/soil_effects.html')

def soil_solutions(request):
    return render(request, 'AgricultureDetails/soil_solutions.html')

def cover_types(request):
    return render(request, 'AgricultureDetails/cover_types.html')

def root_practices(request):
    return render(request, 'AgricultureDetails/root_practices.html')

def diverse_strategies(request):
    return render(request, 'AgricultureDetails/diverse_strategies.html')

def diverse_benefits(request):
    return render(request, 'AgricultureDetails/diverse_benefits.html')

def diverse_limitations(request):
    return render(request, 'AgricultureDetails/diverse_limitations.html')

def livestock_benefits(request):
    return render(request, 'AgricultureDetails/livestock_benefits.html')

def livestock_limitations(request):
    return render(request, 'AgricultureDetails/livestock_limitations.html')