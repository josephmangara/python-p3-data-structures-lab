spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]
# names = get_names(spicy_foods)
# print(names)

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]
spiciest_foods = get_spiciest_foods(spicy_foods)
# print(spiciest_foods)

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        emoji = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {emoji}")
# print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        emoji = "🌶" * heat_level
        if heat_level > 5:
            print(f"{name} ({cuisine}) | Heat Level: {emoji}")
print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    num_foods = len(spicy_foods)
    if num_foods == 0:
        return 0
    return total_heat // num_foods
print(get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    name = spicy_food["name"]
    cuisine = spicy_food["cuisine"]
    heat_level = spicy_food["heat_level"]

    spicy_foods.append({
        "name": name,
        "cuisine": cuisine,
        "heat_level": heat_level,
    })

    return spicy_foods

# Test the function
new_spicy_foods = create_spicy_food(
    [
        {
            "name": "Green Curry",
            "cuisine": "Thai",
            "heat_level": 9,
        },
        {
            "name": "Buffalo Wings",
            "cuisine": "American",
            "heat_level": 3,
        },
        {
            "name": "Mapo Tofu",
            "cuisine": "Sichuan",
            "heat_level": 6,
        },
    ],
    {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
)

print(new_spicy_foods)
