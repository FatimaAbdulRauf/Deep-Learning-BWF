#message
def display_message():
    print("I'm learning about functions in this chapter!")
print(display_message())

#favorite book
def favorite_book(title):
    print("My favorite book is", title)
print(favorite_book("The Broken Window"))

#t-shirts
def make_shirt(size="large", text="I love Python"):
    return "The size of the shirt is " + size + " and it has "+ \
          text + " written on it."
print(make_shirt())
print(make_shirt("medium"))
print(make_shirt(text="keyword arguments", size="small"))

#cities
def describe_city(city, country="Pakistan"):
    return city.title()+ " is in "+ country.title()+"."
print(describe_city("Multan"))
print(describe_city("florence", "italy"))
print(describe_city("nuuk","greenland"))