class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print("Restaurant name is "+ self.restaurant_name \
             + " with cuisine "+ self.cuisine + " and", self.number_served, \
             "customers served!")
        
    def open_restaurant(self):
        return self.restaurant_name + " is open!" 
    
    def set_number_served(self, number):
        self.number_served = number
        print(self.number_served, "customers served by", self.restaurant_name)

    def increment_number_served(self, add_number):
        self.number_served += add_number
        print(self.restaurant_name, "served a total of", self.number_served,\
               "customers after serving", add_number, "more!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, number_served, *flavors):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = flavors
    
    def display_flavor(self):
        flavors= str(self.flavors).split(",")
        print(flavors)

test1 = IceCreamStand("Grub N Go", "Crickets & Cream", 30,"crickets and cream,\
 chocolate critters")
test2 = Restaurant("Upside-Downington", "upside-down desserts", 40)
test3 = Restaurant("Drinks & Co", "apple blood", 50)

print(test1.restaurant_name)
print(test1.cuisine)
print(test1.open_restaurant())
print(test1.describe_restaurant())
print(test2.describe_restaurant())
print(test3.describe_restaurant())
print(test3.set_number_served(34))
print(test2.increment_number_served(10))

print(test1.display_flavor())