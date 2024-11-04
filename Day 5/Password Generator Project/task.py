import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# password = ''
# if nr_symbols == 0 or nr_numbers ==0 or nr_letters == 0:
#     print('Invalid entry. Your password must have at least one letter, one number and one symbol')
# else:
#     for l in range(1,nr_letters+1):
#         password = password + random.choice(letters)
#     for n in range(1,nr_numbers+1):
#         password = password + random.choice(numbers)
#     for s in range(1,nr_symbols+1):
#         password = password + random.choice(symbols)
# print(password)
password_list =[]
if nr_symbols == 0 or nr_numbers ==0 or nr_letters == 0:
    print('Invalid entry. Your password must have at least one letter, one number and one symbol')
else:
    for l in range(1,nr_letters+1):
        password_list.append(random.choice(letters))
    for n in range(1,nr_numbers+1):
        password_list.append(random.choice(numbers))
    for s in range(1,nr_symbols+1):
        password_list.append(random.choice(symbols))
    random.shuffle(password_list)
    password = ''
    for char in password_list:
        password += char
    print('Your password: ', password)


