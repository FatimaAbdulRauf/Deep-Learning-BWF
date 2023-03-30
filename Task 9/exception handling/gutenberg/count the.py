def count_the(filename):
    """Count the number of times 'the' appears in a file"""
    try:
        with open(filename) as file_obj:
            read_content = file_obj.read()
    except FileNotFoundError:
        pass
    else:
        #count the number of times "the" is used in file
        words = read_content.split()
        num_word = words.count("the")
        print("The word 'the' appears about "+ str(num_word) + \
        " times in the file.")

three_little_kittens = "C:\\Users\\LC\\OneDrive\\Documents\\BTW Deep Learning\
\\Task 9\\exception handling\\gutenberg\\three little kittens.txt"
winnie_the_pooh = "C:\\Users\\LC\\OneDrive\\Documents\\BTW Deep Learning\
\\Task 9\\exception handling\\gutenberg\\winnie the pooh.txt"

print(count_the(three_little_kittens))
print(count_the(winnie_the_pooh))