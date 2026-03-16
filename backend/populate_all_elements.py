import os
import django
import sys
import requests

# Setup django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from periodic_table.models import Element

def populate():
    print("Fetching element data from public repository...")
    url = "https://raw.githubusercontent.com/Bowserinator/Periodic-Table-JSON/master/PeriodicTableJSON.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"Failed to fetch data: {e}")
        return
    
    elements_data = data.get('elements', [])
    
    print(f"Found {len(elements_data)} elements. Populating database...")
    
    for item in elements_data:
        # Standardize category strings to match our CSS mappings roughly
        category = item.get('category', 'Unknown').title()
        
        # e.g., "Diatomic Nonmetal" -> "Nonmetal"
        if "Nonmetal" in category:
            category = "Nonmetal"
        elif "Alkali Metal" in category:
            category = "Alkali Metal"
        elif "Alkaline Earth Metal" in category:
            category = "Alkaline Earth Metal"
        elif "Transition Metal" in category:
            category = "Transition Metal"
        elif "Post-Transition Metal" in category:
            category = "Post-transition Metal"
        elif "Metalloid" in category:
            category = "Metalloid"
        elif "Halogen" in category:
            category = "Halogen"
        elif "Noble Gas" in category:
            category = "Noble Gas"
        elif "Lanthanide" in category:
            category = "Lanthanide"
        elif "Actinide" in category:
            category = "Actinide"
        
        # The fields might be null in JSON, so we provide fallbacks
        atomic_mass = item.get('atomic_mass', 0.0)
        if atomic_mass is None: atomic_mass = 0.0
            
        electronegativity = item.get('electronegativity_pauling', None)
        density = item.get('density', None)
        melt = item.get('melt', None)
        boil = item.get('boil', None)
        phase = item.get('phase', '')
        
        # We try to get 'atomic_radius' if present, or None
        atomic_radius = item.get('atomic_radius', None)
        
        Element.objects.update_or_create(
            atomic_number=item['number'],
            defaults={
                'name': item['name'],
                'symbol': item['symbol'],
                'atomic_mass': atomic_mass,
                'group': item.get('xpos', 1),
                'period': item.get('ypos', 1),
                'category': category,
                'electron_configuration': item.get('electron_configuration', ''),
                'electronegativity': electronegativity,
                'atomic_radius': atomic_radius,
                'density': density,
                'melt': melt,
                'boil': boil,
                'phase': phase,
                'description': item.get('summary', '')[:1000] # Ensure it fits
            }
        )
    print(f"Database populated with {len(elements_data)} elements successfully.")

if __name__ == '__main__':
    populate()
