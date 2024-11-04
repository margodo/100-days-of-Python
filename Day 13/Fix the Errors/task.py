try:
    age = int(input("How old are you?"))
except ValueError:
    print('You have types an invalid number. Try numerical value.')
    age = int(input('How old are you?'))
if age > 18:
    print(f"You can drive at age {age}.")
