class Users():
    def __init__(self, f_name, l_name, age, gender, login):
        self.first_name = f_name
        self.last_name = l_name
        self.age = str(age)
        self.gender = gender
        self.login_attempts = login
    def describe_user(self):
        return "First Name: " + self.first_name + \
            "\n Last name: " + self.last_name + "\n Age: " + self.age + \
            "\n Gender: " + self.gender
    def greet_user(self):
        return "Hello " + self.first_name + " " + self.last_name + "!"
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(Users):
    def __init__(self, f_name, l_name, age, gender, login):
        super().__init__(f_name, l_name, age, gender, login)
        self.priviledges = ["can add post", "can delete post", "can ban user"]
    def show_priviledges(self):
        return self.priviledges

luz = Users("Luz", "Noceda", 16, "Female", 2)
mabel = Users("Mabel", "Pines", 12, "Female", 2)
anne = Admin("Anne", "Boonchoy", 18, "Female", 1)

print(anne.show_priviledges())

print(luz.describe_user())
print(luz.greet_user())
print(mabel.describe_user())
print(mabel.greet_user())

#increment login attempts
print(luz.increment_login_attempts())
print(luz.increment_login_attempts())
print(luz.increment_login_attempts())
print(luz.increment_login_attempts())

print("Number of login attempts", luz.login_attempts)

#rest login attempts
print(luz.reset_login_attempts())

print("Number of login attempts",luz.login_attempts)