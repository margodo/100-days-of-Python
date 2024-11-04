programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    'Loop': 'the action of doing something over and over again'
}
print(programming_dictionary["Function"])
print(programming_dictionary.get("Bug"))
programming_dictionary['Lala'] = 'laksmldn'
print(programming_dictionary)

for key in programming_dictionary:
    print(key,': ',programming_dictionary[key])