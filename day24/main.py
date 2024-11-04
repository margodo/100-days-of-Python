with open("../../my_file.txt") as file:
    # contents = file.read()
    print(file.read())

with open("new_file.txt", "w") as file:
    # contents = file.read()
    file.write("Wow")

# r = read
# w = write (rewrite content)
# a = append