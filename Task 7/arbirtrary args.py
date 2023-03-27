def make_sandwich(*ingredients):
    """sandwich items"""
    print("Your sandwich includes:")
    for i in ingredients:
        print("-"+i)
print(make_sandwich("chilli","pepper","olives","chicken"))
print(make_sandwich("chicken","cucumber"))

def car_info(made_by, model, **info):
    """information of a car"""
    information = {}
    information["manufacturer"] = made_by
    information["model_name"] = model
    for key, value in info.items():
        information[key] = value
    return information
car = car_info("sabaru", "outback", color="purple", tow_package= True)
print(car)