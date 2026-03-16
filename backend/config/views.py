from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import json
import os

def index(request):
    """
    Render the interactive periodic table as the homepage.
    """
    return render(request, 'periodic_table.html')

def simulations(request):
    """
    Render the bond simulation workspace.
    """
    return render(request, 'simulations.html')

def dashboard(request):
    """
    Render the user dashboard.
    """
    return render(request, 'dashboard.html')

def atom_viewer(request):
    """
    Render the interactive orbital/circular atom configuration viewer.
    """
    return render(request, 'atom_viewer.html')

def atom_builder(request):
    """
    Render the interactive atom builder exercise page.
    """
    return render(request, 'atom_builder.html')

from learning.models import Lesson, Quiz, StudentProgress

def learning(request):
    """
    Render the gamified learning path dashboard.
    """
    lessons = Lesson.objects.all().order_by('order')
    return render(request, 'learning.html', {'lessons': lessons})

def lesson_detail(request, lesson_id):
    """
    Render the detailed view for a specific lesson.
    """
    lesson = Lesson.objects.get(id=lesson_id)
    return render(request, 'lesson_detail.html', {'lesson': lesson})

def learning_game(request):
    """
    Render the interactive conductivity assessment game.
    """
    return render(request, 'learning_game.html')




def recipes_api(request):
    """
    Serve the 10,000 generated crafting recipes via a paginated JSON API.
    """
    try:
        json_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'recipes.json')
        with open(json_path, 'r') as f:
            data = json.load(f)
            
        # Filtering
        category = request.GET.get('category')
        if category:
            data = [r for r in data if r.get('category', '').lower() == category.lower()]

        # Search
        search = request.GET.get('search')
        if search:
            search = search.lower()
            data = [r for r in data if search in r.get('name', '').lower() or search in r.get('desc', '').lower()]

        # Basic pagination: ?page=1&limit=50
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 50))
        
        start = (page - 1) * limit
        end = start + limit
        
        paginated_data = data[start:end]
        
        return JsonResponse({
            'count': len(data),
            'page': page,
            'limit': limit,
            'total_pages': (len(data) + limit - 1) // limit,
            'results': paginated_data
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
