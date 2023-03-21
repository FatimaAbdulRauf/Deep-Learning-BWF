car_input = str(input("Which rental car would you like? "))
print("Let me see if I can find you a", car_input)

num_people = int(input("Enter number of people in your dinner group: "))
if num_people > 8:
    print("Please wait for your table.")
else:
    print("Your table is ready")

num = int(input("Enter a number to check if it is a multiple of 10: "))
if num%10 == 0:
    print(num, "is a multiple of 10.")
else:
    print(num, "is not a multiple of 10")