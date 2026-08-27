# Dictionary
# Program 1
'''student = {
    "name": "Yash",
    "age": 15,
    "city": "Nashik"
}
print(student["name"])
print(student["city"])

# Program 2
student = {
    "name": "Yash",
    "age": 15
}
student["Course"] = "Python"  # add
print(student)

# Program 3
student = {
    "name": "Yash",
    "age": 15
}
student["age"] = 16  # update
print(student)

# Program 4
student = {
    "name": "Yash",
    "age": 15,
    "city": "Nashik"
}
del student["city"]
print(student)

# Program 5
student = {
    "name": "Yash",
    "age": 15,
    "course": "Python"
}
print(student["name"])    # name
student["age"] = 16       # update
print(student)
student["city"] = "Nashik"   # add
print(student)
del student["course"]    # delete
print(student)

# dictionary methods
student = {
    "name": "Yash",
    "age": 15,
    "city": "Nashik"
}
print(student.keys())
print(student.values())
print(student.items())
print(student.get("color"))'''

'''# Dictionary with for loop
marks = {
    "Maths ": 90,
    "Science ": 85,
    "English ": 88
}
for key in marks:
    print(key)

for value in marks.values():
    print(value)

for key , value in marks.items():
    print(key ,"=", value)'''

'''# Dictionary with if lese
marks = {
    "Maths": 90,
    "Science": 65,
    "English": 82
}

# check maths marks
if marks["Maths"] > 80:
    print("Maths marks are good")
else:
    print("Maths marks are low")

# print subject which is more than 80
for subject, marks in marks.items():
    if marks > 80:
        print(subject, "=", marks)

# check subject pass/fail
for subject, mark in marks.items():
    if mark >= 40:
        print(subject, "Pass")
    else:
        print(subject, "Fail")'''

'''# Dictionary practice set
marks = {
    "Maths": 95,
    "Science": 72,
    "English": 38,
    "History": 85
}
# Q1
print(marks["Maths"])  # maths marks
# Q2
marks["geography"] = 78   # add geography = 78
print(marks)
# Q3
marks["English"] = 45     # update english marks
print(marks)
# Q4
del marks["Science"]
print(marks)
# Q5
for key in marks.keys():    # print kay
    print(key)
# Q6
for value in marks.values():  # print value
    print(value)
# Q7
for key, value in marks.items():   # print key = value pair
    print(key,"=" ,value)

# Q8
for subject,marks in marks.items():
    if marks >= 40:
        print(subject, "Pass")
    else:
        print(subject, "Fail")

# Q9
for subject,marks in marks.items():
    if marks >= 80:
       print(subject,"=",marks)

# Q10
print( "geography" in marks)  # false'''





