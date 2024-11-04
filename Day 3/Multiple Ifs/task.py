print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    price = 0
    if age <= 12:
        print("Children ticket price is $5.")
        price = 5
    elif age <= 18:
        print("Youth ticket price is $7.")
        price = 7
    else:
        print("Adult ticket price is $12.")
        price = 12
    photo = input('Would you like to have a photo? That would be 2$. Type y for yes and n for no')
    if photo == 'y':
        price += 2
    print(f'Your total would be {price}')
else:
    print("Sorry you have to grow taller before you can ride.")
