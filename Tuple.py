# Tuple
# Program 1
numbers = (10, 20, 30, 40, 50)
print(numbers[2])    # print 30
print(numbers[-1])   # print 50
print(numbers[1:4])   # print 20,30,40
print(len(numbers))    # length of list

# using count()
# Program 2
numbers = (10, 20, 30, 20, 40, 20, 50)
print(numbers.count(20))   

# using index()
# Program 3
numbers = (10, 20, 30, 40, 50)
print(numbers.index(40))

# tuple with for loop
numbers = (10, 20, 30, 40, 50)
for num in numbers:
    print(num)

# print odd numbers
numbers = (10, 15, 20, 25, 30, 35, 40)
for num in numbers:
    if num % 2 != 0:
     print(num)

# count even numbers
numbers = (10, 15, 20, 25, 30, 35, 40)
count = 0
for num in numbers:
   if num % 2 == 0:
      count += 1
print("Even numbers =",count)

# Tuple Unpacking
# Program 1
data = ("Python", 100)
langauage , students = data
print("Language =",langauage)
print("Students =",students)

# Program 2
person = ("Akshada", 16, "Nashik")
name, age, city = person
print("Name =",name)
print("Age =",age)
print("City =",city)

# Nested tuple
data = ("Python", (10, 20, 30), "Programming")
print(data[1])                 # inner tuple
print(data[1][1])              # print 20
print(data[2])                 # programming

# Practice test 
# Question 1
numbers = (10, 20, 30, 40, 50)
print(numbers[2])
print(numbers[-1])

# Question 2
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])

# Question 3
numbers = (10, 20, 30, 40, 50)
print(len(numbers))

# Question 4
numbers = (10, 20, 30, 20, 40, 20)
print(numbers.count(20))

# Question 5
numbers = (10, 20, 30, 40, 50)
print(numbers.index(40))

# Question 6
numbers = (10, 20, 30, 40, 50)
for num in numbers:
  print(num)

# Question 7
numbers = (10, 15, 20, 25, 30, 35, 40)
for num in numbers:
   if num % 2 != 0:
      print(num)

# Question 8
numbers = (10, 15, 20, 25, 30, 35, 40)
count = 0
for num in numbers:
   if num % 2 == 0:
      count += 1
print("Count of even number =",count)

# Question 9
numbers = (10, 20, 30, 40, 50)
total = 0
for num in numbers:
   total = total + num
print("Sum =",total)

# Question 10
student = ("Python", 100)
language , students = student
print("Language =",language)
print("Students =",students)

# Question 11
person = ("Yash", 17, "India")
name, age, country = person
print("Name =",name)
print("Age =",age)
print("Country =",country)

# Question 12
data = ("Python", (10, 20, 30, 40), "Programming")
print(data[1][-1])

# Question 13
numbers = (5, 10, 15, 20, 25, 30)
total = 0
for num in numbers:
   if num % 2 == 0:
      total = total + num
print("Sum of even numbers =",total)

numbers = {10, 20, 30, 40}

for num in numbers:
    print(num)

