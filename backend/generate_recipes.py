import os
import django
import sys
import random
import json

# Setup django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from periodic_table.models import Element

# We will generate thousands of random compound recipes to serve as "Macro Materials"
# In a real app we'd query PubChem, but for educational purposes we can algorithmically generate
# plausible sounding compounds and real ones by mixing elements.

def get_standard_recipes():
    return [
        {
            "name": "Water",
            "desc": "A vital chemical compound for all known forms of life.",
            "category": "Material",
            "emoji": "💧",
            "ingredients": {"H": 2, "O": 1}
        },
        {
            "name": "Carbon Dioxide",
            "desc": "A clear gas that is a byproduct of metabolism and combustion.",
            "category": "Material",
            "emoji": "☁️",
            "ingredients": {"C": 1, "O": 2}
        },
        {
            "name": "Sodium Chloride",
            "desc": "Common table salt, essential for life and used for seasoning.",
            "category": "Material",
            "emoji": "🧂",
            "ingredients": {"Na": 1, "Cl": 1}
        },
        {
            "name": "Methane",
            "desc": "The simplest alkane and the main constituent of natural gas.",
            "category": "Fuel",
            "emoji": "🔥",
            "ingredients": {"C": 1, "H": 4}
        },
        {
            "name": "Ammonia",
            "desc": "A colorless gas with a characteristic pungent smell, used in fertilizers.",
            "category": "Material",
            "emoji": "🧪",
            "ingredients": {"N": 1, "H": 3}
        },
        {
            "name": "Glucose",
            "desc": "A simple sugar that is an important energy source in living organisms.",
            "category": "Food",
            "emoji": "🍭",
            "ingredients": {"C": 6, "H": 12, "O": 6}
        },
        {
            "name": "Ethanol",
            "desc": "A volatile, flammable, colorless liquid with a slight characteristic odor.",
            "category": "Material",
            "emoji": "🍷",
            "ingredients": {"C": 2, "H": 6, "O": 1}
        },
        {
            "name": "Sulfuric Acid",
            "desc": "A highly corrosive, strong mineral acid.",
            "category": "Material",
            "emoji": "☣️",
            "ingredients": {"H": 2, "S": 1, "O": 4}
        },
        {
            "name": "Hydrochloric Acid",
            "desc": "A colorless, highly pungent solution of hydrogen chloride in water.",
            "category": "Material",
            "emoji": "🧪",
            "ingredients": {"H": 1, "Cl": 1}
        },
        {
            "name": "Oxygen Molecule",
            "desc": "Diatomic oxygen, essential for aerobic respiration.",
            "category": "Material",
            "emoji": "🌬️",
            "ingredients": {"O": 2}
        },
        {
            "name": "Nitrogen Molecule",
            "desc": "Diatomic nitrogen, making up about 78% of Earth's atmosphere.",
            "category": "Material",
            "emoji": "🌬️",
            "ingredients": {"N": 2}
        }
    ]

def generate_recipes(count=10000):
    print("Fetching elements...")
    elements = list(Element.objects.all())
    if not elements:
        print("No elements in database. Run populate_all_elements.py first.")
        return

    metals = [e for e in elements if 'Metal' in e.category or 'Lanthanide' in e.category or 'Actinide' in e.category]
    nonmetals = [e for e in elements if 'Nonmetal' in e.category or 'Halogen' in e.category]
    metalloids = [e for e in elements if 'Metalloid' in e.category]
    
    recipes = []
    
    print(f"Generating {count} recipes...")
    
    # Let's create some standard templates
    def make_salt():
        m = random.choice(metals)
        nm = random.choice(nonmetals)
        return {
            "name": f"{m.name} {nm.name[:-2] if nm.name.endswith('ine') else nm.name}ide",
            "desc": f"An ionic salt crystal formed by neutralising {m.name} and {nm.name}.",
            "category": "Material",
            "emoji": "💎",
            "ingredients": {m.symbol: random.randint(1, 3), nm.symbol: random.randint(1, 4)}
        }
        
    def make_alloy():
        m1 = random.choice(metals)
        m2 = random.choice(metals)
        while m1 == m2: m2 = random.choice(metals)
        return {
            "name": f"{m1.name}-{m2.name} Alloy",
            "desc": f"A metallic alloy utilized in heavy industry, combining the properties of {m1.name} and {m2.name}.",
            "category": "Material",
            "emoji": "⚙️",
            "ingredients": {m1.symbol: random.randint(1, 5), m2.symbol: random.randint(1, 5)}
        }
        
    def make_organic():
        c = next((e for e in elements if e.symbol == 'C'), None)
        h = next((e for e in elements if e.symbol == 'H'), None)
        o = next((e for e in elements if e.symbol == 'O'), None)
        n = next((e for e in elements if e.symbol == 'N'), None)
        
        ingredients = {c.symbol: random.randint(2, 20), h.symbol: random.randint(4, 40)}
        if random.random() > 0.3 and o: ingredients[o.symbol] = random.randint(1, 6)
        if random.random() > 0.7 and n: ingredients[n.symbol] = random.randint(1, 4)
        
        return {
            "name": f"Complex Hydrocarbon Chain {len(recipes)}",
            "desc": "An organic macromolecule that can be used in plastics, fuels, or synthesis.",
            "category": "Material",
            "emoji": "🧪",
            "ingredients": ingredients
        }
        
    def make_semiconductor():
        base = random.choice(metalloids)
        dopant = random.choice(nonmetals + metals)
        return {
            "name": f"Doped {base.name} Semiconductor",
            "desc": "A fundamental electronic component utilized in logic gates and modern microchips.",
            "category": "Device Part",
            "emoji": "🖥️",
            "ingredients": {base.symbol: random.randint(3, 8), dopant.symbol: 1}
        }
        
    def make_medicine():
        c = next((e for e in elements if e.symbol == 'C'), None)
        h = next((e for e in elements if e.symbol == 'H'), None)
        o = next((e for e in elements if e.symbol == 'O'), None)
        n = next((e for e in elements if e.symbol == 'N'), None)
        s = next((e for e in elements if e.symbol == 'S'), None)
        
        ingredients = {c.symbol: random.randint(6, 25), h.symbol: random.randint(8, 30)}
        if o: ingredients[o.symbol] = random.randint(1, 8)
        if n: ingredients[n.symbol] = random.randint(1, 5)
        if random.random() > 0.8 and s: ingredients[s.symbol] = random.randint(1, 2)
        
        return {
            "name": f"Synthetic Therapeutic Agent-{len(recipes)}",
            "desc": "A biologically active pharmaceutical molecule used to treat ailments.",
            "category": "Medicine",
            "emoji": "💊",
            "ingredients": ingredients
        }

    def make_food():
        c = next((e for e in elements if e.symbol == 'C'), None)
        h = next((e for e in elements if e.symbol == 'H'), None)
        o = next((e for e in elements if e.symbol == 'O'), None)
        
        # like sugars C6H12O6
        ingredients = {c.symbol: random.randint(4, 12), h.symbol: random.randint(8, 24), o.symbol: random.randint(4, 12)}
        
        return {
            "name": f"Carbohydrate/Lipid Nutrient {len(recipes)}",
            "desc": "An energy-dense macronutrient processed by organisms for metabolism.",
            "category": "Food",
            "emoji": random.choice(["🍞", "🥩", "🍎", "🧀"]),
            "ingredients": ingredients
        }

    generators = [make_salt, make_alloy, make_organic, make_semiconductor, make_medicine, make_food]
    
    # Prepend standard recipes
    standard_recipes = get_standard_recipes()
    for i, recipe in enumerate(standard_recipes):
        recipe['id'] = f"std_recipe_{i}"
        recipes.append(recipe)
    
    print(f"Added {len(standard_recipes)} standard recipes.")
    
    for i in range(count - len(standard_recipes)):
        gen = random.choice(generators)
        recipe = gen()
        recipe['id'] = f"recipe_{i}"
        recipes.append(recipe)
        
        if (i+1) % 1000 == 0:
            print(f"Generated {i+1}...")

    # Write to a JSON file rather than exploding the frontend memory statically
    # The frontend will fetch this via AJAX pagination or a direct massive load.
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'recipes.json')
    with open(out_path, 'w') as f:
        json.dump(recipes, f)
        
    print(f"Successfully wrote {count} recipes to {out_path}.")

if __name__ == '__main__':
    generate_recipes(10000)
