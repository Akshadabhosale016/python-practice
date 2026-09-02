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

''''# Dictionary practice
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
    print("Fail")'''

'''# Q1  Highest marks
marks = {
    "Maths": 85,
    "Science": 92,
    "English": 78,
    "History": 88
}
highest = 0
highest_subject = ""
for subject, mark in marks.items():
    if mark > highest:
        highest = mark
        highest_subject = subject
print(highest_subject,"=",highest)

# Q2
marks = {
    "Maths": 85,
    "Science": 32,
    "English": 78,
    "History": 25,
    "Geography": 65
}
count = 0
for subject , mark in marks.items():
    if mark >= 40:
        count += 1
print("Pass subject =",count)

# Q3
marks = {
    "Maths": 85,
    "Science": 32,
    "English": 78,
    "History": 25,
    "Geography": 65
}
for subject , mark in marks.items():
    if mark < 40:
      print(subject,"=",mark)

# Q4
marks = {
    "Maths": 85,
    "Science": 92,
    "English": 78,
    "History": 88
}
total = 0
for subject, mark in marks.items():
    total = total + mark
print("Total marks =",total)

# Q5
marks = {
    "Maths": 85,
    "Science": 92,
    "English": 78,
    "History": 88
}
total = 0
count = 0
for subject, mark in marks.items():
    count += 1
    total = total + mark
    avg = total / count
print("Total marks =",total)
print("Average =",avg)

# lowest marks
marks = {
    "Maths": 85,
    "Science": 92,
    "English": 78,
    "History": 88
}
lowest = 999
lowest_subject = ""
for subject, mark in marks.items():
    if mark < lowest:
        lowest = mark
        lowest_subject = subject
print("Lowest =",lowest_subject ,"=",lowest)

# Search subject
marks = {
    "Maths": 85,
    "Science": 92,
    "English": 78,
    "History": 88
}
subject = input("Enter subject :")
if subject in marks:
    print(subject,"=",marks[subject])
else:
    print("Subject NOT found")

# Grade calculator
marks = {
    "Maths": 85,
    "Science": 92,
    "English": 78,
    "History": 88
}
for subject, mark in marks.items():
    if mark >= 90:
        grade = "A"
        print(subject,"=",grade)
    elif mark >= 75:
        grade = "B"
        print(subject,"=",grade)
    elif mark >= 60 :
        grade = "C"
        print(subject,"=",grade)
    elif mark >= 40:
        grade = "D"
        print(subject,"=",grade)
    else:
        grade = "F"
        print(subject,"=",grade)'''

'''# Student result analyzer
marks = {
    "Maths": 85,
    "Science": 92,
    "English": 38,
    "History": 88,
    "Geography": 72
}
total = 0
count = 0
pass_sub = 0
fail_sub = 0
highest = 0
highest_subject = ""
lowest = 999
lowest_subject = ""
for subject, mark in marks.items():
    if mark > highest:
        highest = mark
        highest_subject = subject
    if mark < lowest:
        lowest = mark
        lowest_subject = subject
    if mark > 40:
        pass_sub += 1
    else:
        fail_sub += 1
    
    count += 1
    total = total + mark
avg = total / count
print("Total marks =",total)
print("Average =",avg)
print("Highest =",highest_subject,"=",mark)
print("Lowest =",lowest_subject,"=",lowest)
print("Pass subject =",pass_sub)
print("Fail subject =",fail_sub)

# Find Students Who Scored Above Average
marks = {
    "Yash": 85,
    "Rahul": 92,
    "Amit": 65,
    "Sneha": 78,
    "Priya": 90
}
total = 0
count = 0
for student, mark in marks.items():
    total = total + mark
    count += 1
    avg = total / count 
print("Total marks =",total)
print("Count student =",count)
print("Average =",avg)

for student, mark in marks.items():
    if mark > avg:
        print(student, "=", mark)'''

'''# Count frequency of number
numbers = [10, 20, 10, 30, 20, 10, 40, 30]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print(frequency)

# word frequency
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
frequency ={}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print(frequency)'''

'''# most frequent word
words = ["apple", "banana", "apple", "orange", "banana", "apple", "orange"]
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
highest = 0
highest_word = ""
for word, count in frequency.items():
    if count > highest:
        highest = count
        highest_word = word
print("Frequency =",highest)
print("More frequent word =",highest_word)'''

'''# most frequent character
text = "programming"
frequency = {}
for character in text:
    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1
highest = 0
highest_character = ""
for character, alpha in frequency.items():
    if alpha > highest:
        highest = alpha
        highest_character = character
print("most frequent character =",highest_character)
print("Frequency =",highest)

# Find duplicate values
marks = {
    "Yash": 85,
    "Rahul": 92,
    "Amit": 85,
    "Sneha": 78,
    "Priya": 92
}
frequency = {}
for mark, count in marks.items():
    if mark in frequency:
        frequency[mark] += 1
    else:
        frequency[mark] = 1
for mark, count in frequency.items():
    if count > 1:
        print(mark,)'''

'''a = int(input("Enter first number ="))
b = int(input("Enter second number="))
print("Sum =",a+b)
print("Product =",a*b)

name = "Yash"
age = 18
height = 5.8
is_student = True
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

length = int(input("Enter length : "))
width = int(input("Enter width : "))
area = length * width
perimeter = 2 * (length + width)
print("Area = ",area)
print("Periemeter = ",perimeter)

num = int(input("Enter a number : "))
print("Square = ",num*num)
print("Cube = ",num*num*num)
print("Double = ",num*2)
print("Half = ", num/2)

num = int(input("Enter a number : "))
if num % 2 == 0:
    print(num,"is EVEN number")
else:
    print(num,"is ODD number")

num = int(input("Enter a number : "))
if num > 0:
    print(num,"is POSITIVE number")
elif num < 0:
    print(num,"is NEGATIVE number")
else:
    print(num,"is ZERO")

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
if a > b and a > c :
    print(a, "is largest")
elif b > c and b > a:
    print(b," is largest")
else:
    print(c, "is largest")

year = int(input("Enter a year"))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(year, "is leap year")
else:
    print(year, "is NOT leap year")

num = int(input("Enter a number = "))
fact = 1
while num > 0:
    fact = fact*num
    num = num - 1
print(fact)

num = int(input("Enter a number : "))
total = 0
while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10
print(total)

num = int(input("Enter a number : "))
count = 0
while num > 0:
    count += 1
    num = num // 10
print(count)

num = int(input("Enter a number : "))
smallest = num % 10
num = num // 10
while num > 0:
    digit = num % 10
    if digit < smallest:
        smallest = digit
    num = num // 10
print(smallest,"is smallest")

# armstrong number
num = int(input("Enter a number : "))
original = num
total = 0
while num > 0:
    digit = num % 10
    total = total + digit**3
    num = num // 10
if total == original:
    print(original, "is armstrong number")
else:
    print(original, "is NOT armstrong number")

text = input("Enter a text : ")
text = text.lower()
print(text.count("a"))'''

text = input("Enter some text :")
print(text.strip().lower().replace(" ",""))





 












