# List comprehension
import random

# numbers = [1,7,24,5]
# new_list = [n + 1 for n in numbers]
# print(new_list)
# numbers = [1,2,3]
# new_list = [n+1 for n in numbers]
# print(new_list)
# name = 'Alex'
# letters = [letter for letter in name]
# doubled_numbers = [i * 2 for i in range(1,5)]
# names = ['Alex', 'Bob', 'Carolina', 'Nick','Lora', 'Angela']
# who_goes = [name for name in names if name[0] == 'A']
# who_goes = [name for name in names if len(name) < 5]
# who_goes = [name.upper() for name in names]
# students_score = {name:random.randint(1,100) for name in names}
# print(students_score)
# passed_students = {name:score for (name,score) in students_score.items() if score > 50}
# print(passed_students)

student_dict ={
    "student": ["Bob", "Ashley", "Karl"],
    "score": [56,74,25]
}

import pandas
student_dataframe = pandas.DataFrame(student_dict)
# Loop through the rows
for (index, row) in student_dataframe.iterrows():
    print(row.score)