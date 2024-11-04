# FileNotFound
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     something = a_dictionary["key"]
# except FileNotFoundError:
#     file = open("a_file.txt", 'a')
#     file.write("smth")
# except KeyError as error_message:
#     print(f"This key {error_message} doesn't exist")
# else:
#     content = file.read()
#     print(content)
#     print(something)
# finally:
# # Raise your own exception
#     raise KeyError("My message")

# KeyError
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existing"]

# IndexError
# fruits = ["apple","banana"]
# fruit = fruits[2]

# TypeError
# text = "abc"
# print(text+5)

height = float(input("Height: "))
weight = int(input("Weight: "))
if height > 3:
    raise ValueError("Human height can not be over 3 meters")
bmi = weight /height**2
print(bmi)