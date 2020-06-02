material = {
    'water': 400,
    'milk': 540,
    'coffee': 120,
    'cup': 9,
    'money': 550,
}

type_coffee = {
    'espresso': {
        'water': 250,
        'coffee': 16,
        'money': -4,
    },
    'latte': {
        'water': 350,
        'milk': 75,
        'coffee': 20,
        'money': -7,
    },
    'cappuccino': {
        'water': 200,
        'milk': 100,
        'coffee': 12,
        'money': -6,
    },
}
d1 = {'a': 10, 'b': 9, 'c': 8, 'd': 7}
d2 = {'a': 1, 'b': 2, 'c': 3, 'e': 2}
material = {key: material[key] - type_coffee['espresso'].get(key, 0) for key in material}
print(material)
