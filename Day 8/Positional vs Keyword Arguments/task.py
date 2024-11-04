# Functions with input
name = input('What is your name? ')
loc = input('Where are you form? ')
def greet_with_name(name,location):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f'How is the weather in {location}?')

greet_with_name(name,loc)
greet_with_name(name='Peter', location='London')
