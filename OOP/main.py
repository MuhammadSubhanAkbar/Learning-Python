from car import Car

cars = [
    Car("Ford",      "Mustang",  2025, "Red",   False),
    Car("Chevrolet", "Corvette", 2025, "Blue",   True),
    Car("Dodge",     "Charger",  2025, "Yellow", True)
]

for i in range(len(cars)):
    print(f"Car {i + 1}:")
    cars[i].drive()
    cars[i].sale()

    print()
