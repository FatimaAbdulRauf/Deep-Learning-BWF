def read_files(filename):
    """Read files"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print("Good pet names are:\n",contents)

file1 = "C:\\Users\\LC\\OneDrive\\Documents\\BTW Deep Learning\\Task 9\
\\exception handling\\missing files\\cat names.txt"
file2 = "C:\\Users\\LC\\OneDrive\\Documents\\BTW Deep Learning\\Task 9\
\\exception handling\\missing files\\dogs.txt"
print(read_files(file1))
print(read_files(file2))

