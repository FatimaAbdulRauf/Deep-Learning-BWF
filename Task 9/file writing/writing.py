#writing guest names to a file
guest_file = "guest.txt"
guest_name = input("Enter your name: ")
with open(guest_file, "w") as guest_object:
    guest_object.write(guest_name)

#guest book
guest_book = "guest_book.txt"
while True:
    print("\n Names for guest book: ")
    print("\n Enter q to quit any time: ")
    guest = input("Enter your name: ")
    if guest == "q":
        break
    else:
        print("Hello " + guest+ ", welcome!")
        with open(guest_book, "a") as guest_file:
            guest_file.write(guest + " was a guest here.\n")

#programming poll
reasons = "reasons.txt"
while True:
    print("\n Why do people like programming?")
    print("enter 0 to quit")
    reason = input("Why do you like programming? ")
    if reason == "0":
        break
    else:
        print(reason)
        with open(reasons, "a") as record_file:
            record_file.write(reason+"\n")