print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print('Awesome! You can ride the rollercoaster!')
    age = int(input('How old are you?'))
    if age > 18:
        print('Ticket price is 12$.')
    elif age > 12:
        print('Ticket price is 5$')
    else:
        print('Unfortunately you are too little.')
else:
    print("Sorry you have to grow taller before you can ride.")
