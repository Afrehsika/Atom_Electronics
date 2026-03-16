import os
import django
import sys

# Setup django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from periodic_table.models import Element

def populate():
    elements_data = [
        {"name": "Hydrogen", "symbol": "H", "atomic_number": 1, "atomic_mass": 1.008, "group": 1, "period": 1, "category": "Nonmetal"},
        {"name": "Helium", "symbol": "He", "atomic_number": 2, "atomic_mass": 4.0026, "group": 18, "period": 1, "category": "Noble Gas"},
        {"name": "Lithium", "symbol": "Li", "atomic_number": 3, "atomic_mass": 6.94, "group": 1, "period": 2, "category": "Alkali Metal"},
        {"name": "Beryllium", "symbol": "Be", "atomic_number": 4, "atomic_mass": 9.0122, "group": 2, "period": 2, "category": "Alkaline Earth Metal"},
        {"name": "Boron", "symbol": "B", "atomic_number": 5, "atomic_mass": 10.81, "group": 13, "period": 2, "category": "Metalloid"},
        {"name": "Carbon", "symbol": "C", "atomic_number": 6, "atomic_mass": 12.011, "group": 14, "period": 2, "category": "Nonmetal"},
        {"name": "Nitrogen", "symbol": "N", "atomic_number": 7, "atomic_mass": 14.007, "group": 15, "period": 2, "category": "Nonmetal"},
        {"name": "Oxygen", "symbol": "O", "atomic_number": 8, "atomic_mass": 15.999, "group": 16, "period": 2, "category": "Nonmetal"},
        {"name": "Fluorine", "symbol": "F", "atomic_number": 9, "atomic_mass": 18.998, "group": 17, "period": 2, "category": "Halogen"},
        {"name": "Neon", "symbol": "Ne", "atomic_number": 10, "atomic_mass": 20.180, "group": 18, "period": 2, "category": "Noble Gas"},
        {"name": "Sodium", "symbol": "Na", "atomic_number": 11, "atomic_mass": 22.990, "group": 1, "period": 3, "category": "Alkali Metal"},
        {"name": "Magnesium", "symbol": "Mg", "atomic_number": 12, "atomic_mass": 24.305, "group": 2, "period": 3, "category": "Alkaline Earth Metal"},
        {"name": "Aluminum", "symbol": "Al", "atomic_number": 13, "atomic_mass": 26.982, "group": 13, "period": 3, "category": "Post-transition Metal"},
        {"name": "Silicon", "symbol": "Si", "atomic_number": 14, "atomic_mass": 28.085, "group": 14, "period": 3, "category": "Metalloid"},
        {"name": "Phosphorus", "symbol": "P", "atomic_number": 15, "atomic_mass": 30.974, "group": 15, "period": 3, "category": "Nonmetal"},
        {"name": "Sulfur", "symbol": "S", "atomic_number": 16, "atomic_mass": 32.06, "group": 16, "period": 3, "category": "Nonmetal"},
        {"name": "Chlorine", "symbol": "Cl", "atomic_number": 17, "atomic_mass": 35.45, "group": 17, "period": 3, "category": "Halogen"},
        {"name": "Argon", "symbol": "Ar", "atomic_number": 18, "atomic_mass": 39.95, "group": 18, "period": 3, "category": "Noble Gas"},
    ]
    
    for item in elements_data:
        Element.objects.update_or_create(
            atomic_number=item['atomic_number'],
            defaults=item
        )
    print("Database populated with first 18 elements successfully.")

if __name__ == '__main__':
    populate()
