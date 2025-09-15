def hello():
    name = input("What is your name?").title().strip()
    age = int(input("What is your age?"))

    print(f"Hello,{name}, you are{age} years old")

hello()