from car import Car

cars = [
    Car("Ford",      "Mustang",  2025, "Red",   False),
    Car("Chevrolet", "Corvette", 2025, "Blue",   True),
    Car("Dodge",     "Charger",  2025, "Yellow", True)
]

for i in range(len(cars)):
    print(f"Car {i + 1}:")
    for attributes, value in cars[i].__dict__.items():
        print(f"{attributes}: {value}")
    print()
