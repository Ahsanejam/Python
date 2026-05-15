from tkinter.ttk import Progressbar

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     # "Loop": "The action of doing something over and over again.",
#
# }

# print(programming_dictionary["Function"])

# programming_dictionary["Loops"] = "The action of doing something over and over again."
# print(programming_dictionary["Loops"])

# empty_dictionary = {}

# Wipe an existing dictionary

# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)


# Loop through a dictionary
# for keys, items in programming_dictionary.items():
#     print(keys+": "+items)
# for keys in programming_dictionary:
#     print(keys)
#     print(programming_dictionary[keys])

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# empty = {}
# key = input("Enter your name? ")
# value = int(input("What's your age? "))
# empty[key] = value
# # print(empty)
# for value in empty:
#     print(value)
#     print(empty[value])

max = 0
for key in student_scores:
    if student_scores[key] > max:
        # max = key
        max = student_scores[key]
print(max)

for key in student_scores:
    if max == student_scores[key]:
        print(f"{key}: {student_scores[key]}")
        print()

# student_grades = student_scores
#
# for key in student_grades:
#     Grade = ""
#     if student_grades[key] >= 91 and student_grades[key] <= 100:
#         Grade = "Outstanding"
#     elif student_grades[key] >= 81 and student_grades[key] <= 90:
#         Grade = "Exceeds Expectations"
#     elif student_grades[key] >= 71 and student_grades[key] <= 80:
#         Grade = "Acceptable"
#     else:
#         Grade = "Fail"
#     student_grades[key] = Grade
#
#     print(key)
#     print(student_grades[key])
# print(student_grades)