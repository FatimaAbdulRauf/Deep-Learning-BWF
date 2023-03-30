#addition calculator
print("Enter two numbers for addition!")
print("Enter q to quit")
while True:
    first_number = input("Enter first number: ")
    if first_number == "q":
        break
    second_number = input("Enter second number: ")
    try:
        addition = int(first_number) + int(second_number)
    except ValueError:
        print("You need to enter numbers for addition!")
    else:
        print(addition)
