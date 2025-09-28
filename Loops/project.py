#Define the Main function
def main():
    print_matrics()

#Define the Matrics function
def print_matrics():
    row = int(input("Enter the number of rows: "))
    col = int(input("Enter the number of columns: "))
    char = input("Enter the character: ")

    for i in range(row):
        for j in range(col):
            print(char, end=" ")
        print()

if __name__ == "__main__":
    main()