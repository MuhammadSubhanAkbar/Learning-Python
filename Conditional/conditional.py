#Simple calculator app

print("=== SIMPLE CALCULATOR ===")
print("Operations available:")
print("+ : Addition")
print("- : Subtraction")
print("* : Multiplication")
print("/ : Division")
print("** : Power")
print("% : Modulus")

#Get user input
num_1 = float(input("What is the first number:")) #For number 1
operation =  input("What operation you want:") #For operation
num_2 = float(input("What is the second number:")) #For number 2

#Perform the nessessary calculatoin
if operation == "+":
    result = num_1 + num_2
    print(f"{num_1} + {num_2} = {result}")
elif operation == "-":
    result = num_1- num_2
    print(f"{num_1} - {num_2} = {result}")
elif operation == "*":
        result = num_1*num_2
        print(f"{num_1} * {num_2} = {result}")
elif operation == "/":
         result = num_1 / num_2
         print(f"{num_1} / {num_2} = {result}")
elif operation == "**":
      result = num_1 ** num_2
      print(f"{num_1} ^ {num_2} = {result}")
