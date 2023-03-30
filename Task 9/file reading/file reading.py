filename = "learning_python.txt"
#reading an entire file
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

#looping over file object
with open(filename) as learning_object:
    for row in learning_object:
        print(row.rstrip())

#storing lines in a list
with open(filename) as read_object:
    lines = read_object.readlines()
for line in lines:
    print(line.rstrip())

#replace() method
learning_js = contents.replace("Python", "JavaScript")
print(learning_js)