from django.shortcuts import render, redirect
from core.decision_engine import analyze_meal


def home(request):
    return render(request, 'core/home.html')


def profile(request):
    if request.method == 'POST':
        profile_data = {
            'name': request.POST.get('name', ''),
            'age': request.POST.get('age', ''),
            'weight': request.POST.get('weight', ''),
            'height': request.POST.get('height', ''),
            'gender': request.POST.get('gender', ''),
        }
        request.session['profile_data'] = profile_data
        return redirect('meal_input')
    
    current_profile = request.session.get('profile_data', {})
    return render(request, 'core/profile.html', {'profile': current_profile})


def meal_input(request):
    if request.method == 'POST':
        data = {
            'meal': request.POST.get('meal', ''),
            'goal': request.POST.get('goal', ''),
            'budget': request.POST.get('budget', ''),
            'mode': request.POST.get('mode', ''),
        }
        request.session['meal_data'] = data
        return redirect('result')
    return render(request, 'core/meal_input.html')


def result(request):
    data = request.session.get('meal_data', {})
    if not data:
        return render(request, 'core/result.html', {'result': None})
    
    # Ensure data dict is complete for the engine
    engine_input = {
        'meal': data.get('meal', ''),
        'goal': data.get('goal', ''),
        'budget': data.get('budget', ''),
        'mode': data.get('mode', ''),
    }
    
    analysis_result = analyze_meal(engine_input)
    return render(request, 'core/result.html', {'result': analysis_result})
