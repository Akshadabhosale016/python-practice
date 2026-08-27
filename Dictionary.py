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

'''# Dictionary practice 
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

'''# update method
student = {
    "name": "Yash",
    "age": 15
}
student.update({ "City" : "Nashik",
                "age" : 16,
                "course" :"python",
                "marks" : 90
                })
print(student)

# pop method
student = {
    "name": "Yash",
    "age": 16,
    "city": "Nashik",
    "course": "Python"
}
student.pop("city")  # Q1
print(student)
result = student.pop("course") # Q2
print(result)
print(student)
result = student.pop("marks", "key not found") # Q3
print(result)

# popitem() method
student = {
    "name": "Yash",
    "age": 16,
    "city": "Nashik",
    "course": "Python"
}
student.popitem()  # Q1
print(student)
result = student.popitem()  # Q2
print(result)
print(student)
student.popitem()    # Q3
print(student)
student.popitem()'''

# Dictionary practice
student = {
    "name": "Yash",
    "age": 16,
    "city": "Nashik",
    "marks": 85
}
for key in student.keys():   # print key  Q1
    print(key)
for value in student.values():   # print value Q2
   print(value)
for key, value in student.items():  # print key value pair Q3
    print(key,"=",value)
student.update({"course" : "python"})  # update Q4
print(student)
student.pop("city")     # delete Q5
print(student)
student.popitem()         # popitem() Q6
print(student)
print("email" in student)   # Q8
print(student.get("phone"))  # Q9
student.clear()  # Q10
print(student)
if student["marks"] > 40:    # Q7
    print("Pass")
else:
    print("Fail")









