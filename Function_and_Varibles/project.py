def main():
    x = float(input("What is your total bill: "))
    y = float(input("What is your tip percentage: "))

    z = round((x * y) / 100, 2)
    total = round(z + x, 2)

    print(f"Your tip amount is: {z}")
    print(f"Your total bill is: {total}")

main()
