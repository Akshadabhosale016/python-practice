# def welcome():
#     print("Welcome to python")
# welcome()

# def greet():
#     print("Welcome")
#     print("Welcome to python")
# greet()

# def even_odd():
#     num = 12
#     if num % 2 == 0:
#         print("Even number")
#     else:
#         print("Odd number")
# even_odd()

#Qs 1
# def hello():
#     print("Hello world")
# hello()

# #Qs 2
# def student():
#     print("My name is yash")
#     print("I am learning python")
# student()

# #QS3
# def square():
#     num = 6
#     result = num*num
#     print("Square =",result)
# square()

# #Qs4
# def cube():
#     num = 3
#     result = num*num*num
#     print("Cube =",result)
# cube()

# #Qs5
# def even_odd():
#     num = 12
#     if num % 2 == 0:
#         print("Even number")
#     else:
#         print("Odd number")
# even_odd()

# #Qs6
# def sum():
#     a = 10
#     b = 20
#     result = a + b
#     print("Sum =",result)
# sum()

# #Qs7
# def largest():
#     a = 15
#     b = 25
#     if a > b:
#         print(a,"is largest")
#     else:
#         print(b,"is largest")
# largest()

# #Qs8
# def check_num():
#     num = -5
#     if num > 0:
#         print("Positive")
#     else:
#         print("Negative")
# check_num()

#Qs9
# def factorial():
#     num = 5
#     fact = 1
#     for i in range(1,num+1):
#         fact = fact*i
#     print("Factorial =",fact)
# factorial()

# #Qs10
# def count_even():
#     count = 0
#     for i in range(2,11,2):
#         count += 1
#     print("count =",count)
# count_even()

# Argument
# def greet(name):
#     print("Hello",name)
# greet("Yash")

# def square(num):
#     result = num*num
#     print("Square =",result)
# square(5)
# square(10)

# def add(a,b):
#     result = a + b
#     print("Sum =",result)
# add(10,20)
# add(5,7)

# def student(name,age,city):
#     print("Name =",name)
#     print("Age =",age)
#     print("City =",city)
# student("Yash",18,"Nashik")

# def multiply(a,b):
#     result = a*b
#     print("Product =",result)
# multiply(5,4)
# multiply(10,3)

# def even_odd(num):
#     if num % 2 == 0:
#         print(num ,"Even number")
#     else:
#         print(num,"Odd number")
# even_odd(8)
# even_odd(7)
# even_odd(20)

# def student(name="Python"):
#     print("Hello",name)
# student()
# student("Yash")

# def power(num,exponent = 2):
#     result = num**exponent
#     print("Power =",result)
# power(5)
# power(2,3)

#Question 21
# num = int(input("Enter number ="))
# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# # Question 22
# marks = int(input("Enter marks ="))
# if marks >= 90:
#     print("A Grade")
# elif marks >= 75:
#     print("B Grade")
# elif marks >= 60:
#     print("C Grade")
# elif marks >= 40:
#     print("D Grade")
# else:
#     print("Fail")

# # Question 23
# num = int(input("Enter number ="))
# for i in range(1,11):
#     print(num*i)

# # Question 24
# num = int(input("Enter number ="))
# total = 0
# while num > 0:
#     digit = num % 10
#     total = total + digit
#     num = num + 1
#     num = num // 10
# print("Sum =",total)

# # Question 25
# balance = int(input("Enter account balance ="))
# withdraw = int(input("Enter withdraw amount ="))
# if balance >= 0 and withdraw <= balance:
#     print("Withdrawal Successful !")
# else:
#     print("Unsufficient balance")
# if balance <= 0:
#     print("Account has no balance")

# Argument
# Program 1
# def greeting(name):
#     print("Hello",name)
# greeting("Yash")

# Program 2
# def add(a,b):
#     result = a + b
#     print("Sum =",result)
# add(10,20)

# Program 3
# def student(name,age):
#     print("Name =",name)
#     print("Age =",age)
# student("Yash",18)

# Program 4
# def student(name="Python"):
#     print("Hello",name)
# student()
# student("Yash")

# Program 5
# def power(num,exponent=2):
#     result = num**exponent
#     print("Power =",result)
# power(5)
# power(2,3)

# Part 2 : *args

# Program 6
# def numbers(*args):
#     print(args)
# numbers(10,20,30,40)

# Program 7
# def add(*args):
#     total = 0
#     for i in args:
#         total = total + i
#     print("Sum =",total)
# add(10,20,30,40)

# Program 8
# def numbers(*args):
#     largest = 0
#     for num in args:
#         if num > largest:
#             largest = num
#     print("Largest =",largest)
# numbers(10,50,20,80,30)

# Program 9
# def numbers(*args):
#     count = 0
#     for i in args:
#         count += 1
#     print("Count =",count)
# numbers(10,20,30,40,50)

# Program 10
# def student(name,*marks):
#      total = 0
#      for i in marks:
#           total = total + i
#      print("Name =",name)
#      print("Marks =",marks)
#      print("Total =",total)
# student("Yash",80,85,90)

# Part 3 : **kwargs  
# Program 11
# def student(**kwargs):
#      print(kwargs)
# student(name="yash",age=18,city="nashik")

# Program 12
# def student(**kwargs):
#     for key, value in kwargs.items():
#         print(key, "=", value)

# student(name="Yash", salary=5000, department="IT")

# Program 13
# def person(**kwargs):
#     count = 0
#     for i in kwargs:
#         count += 1
#     print("Count =",count)
# person(name="Yash",age=18,salary=5000)

# Program 14
# def student(**kwargs):
#     for key in kwargs:
#        print(key)
# student(name="Yash", age=18, city="Pune")

 # Program 15
# def student(**kwargs):
#     for value in kwargs.values():
#        print(value)
# student(name="Yash", age=18, city="Pune")

# Part 4 : *arg + **kwargs
# Program 16
# def student(*args,**kwargs):
#     print("Marks =",args)
#     print("Student details =",kwargs)
# student(90,80,85,name="Akshuu",age=21)

# Program 17
# def customer(*args,**kwargs):
#     print("Product price =",args)
#     print("Customer detail =",kwargs)
# customer(600,900,300,name="Akshada",age=21,city="Nashik")

# Program 18
# def employee(*args,**kwargs):
#     total = 0
#     for i in args:
#         total = total + i
#     print("Salary component =",args)
#     print("Employee information =",kwargs)
#     print("Total salary =",total)
# employee(20000,5000,3000,name="Akshada",department="Co")

# Program 20
# def average(*args):
#     total = 0
#     count = 0
#     for i in args:
#         total = total + i
#         count += 1
#     average = total / count
#     print("Count =",count)
#     print("Marks =",total)
#     print("Average =",average)
# average(80,85,90,95)

# program 30
# def employee(*args, **kwargs):
#     total = 0

#     for i in args:
#         total = total + i

#     print("Name =", kwargs["name"])
#     print("Department =", kwargs["department"])
#     print("City =", kwargs["city"])
#     print("Salary Components =", args)
#     print("Total Salary =", total)

# employee(5000, 3000, 2000,
#          name="Yash",
#          department="IT",
#          city="Nashik")
    
# Return statement
# def even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# result = even_odd(8)
# print(result)

# def student(marks):
#     if marks >= 90:
#         return "Grade A"
#     elif marks >= 75:
#         return "Grade B"
#     elif marks >= 60:
#         return "Grade C"
#     elif marks >= 40:
#         return "Grade D"
#     else:
#         return "Fail"
# result = student(76)
# print(result)

# def digit_sum(num):
#     total = 0
#     while num > 0:
#         digit = num % 10
#         total = total + digit
#         num = num // 10
#     return total
# result = digit_sum(583)
# print(result)

# def numbers(*args):
#     largest = 0
#     for num in args:
#         if num > largest:
#             largest = num
#     return largest
# result = numbers(10,50,20,80,30)
# print(result)

# def income(**kwargs):
#     return kwargs["salary"] + kwargs["bonus"]
# result = income(salary=30000,bonus=5000)
# print(result)

# def employee(*args,**kwargs):
#     total = 0
#     for i in args:
#         total = total + i
#     return total
# result = employee(20000,5000,3000,name="Yash",department="IT")
# print(result)

# def net_salary(salary,tax,bonus):
#     return salary - tax + bonus
# result = net_salary(40000,4000,5000)
# print(result)

# def final_amount(amount):
#     if amount >= 5000:
#         discount = amount*0.20
#     elif amount >= 3000:
#         discount = amount*0.10
#     elif amount >= 1000:
#         discount = amount*0.05
#     else:
#         discount = 0
#     return amount - discount
# result = final_amount(5000)
# print(result)

# def student_result(*args):
#     total = 0
#     count = 0
#     for i in args:
#         total = total + i
#         count += 1
#     avg = total / count
#     if avg >= 75:
#         result = "Distinction"
#     elif avg >= 60:
#         result = "First class"
#     elif avg >= 50:
#         result = "Second class"
#     elif avg >= 40:
#         result = "Pass"
#     else:
#         result = "Fail"
#     return result, avg
# result = student_result (80,75,85)
# print(result)

# def emp_salary(basic_salary,bonus,tax):
#     net_salary = basic_salary + bonus - tax
#     if net_salary >= 50000:
#         category = "High salary"
#     elif net_salary >= 30000:
#         category = "Good salary"
#     elif net_salary >= 20000:
#         category = "Average salary"
#     else:
#         category = "Low salary"
#     return category,net_salary
# result = emp_salary(40000,8000,5000)
# print(result)

# E-commerce order calculator
# def customer(amount,discount,delivery_charge):
#     final_amount = amount - discount + delivery_charge
#     if final_amount >= 5000:
#         order = "Premium order"
#     elif final_amount >= 3000:
#         order = "Standard order"
#     elif final_amount >= 1000:
#         order = "Basic order"
#     else:
#         order = "Small order"
#     return final_amount, order
# result = customer(5000,500,100)
# print(result)

# Employee attendance system
# def employee(total_day,present_day):
#     percentage = present_day / total_day*100
#     if percentage >= 90:
#         category = "Excellent"
#     elif percentage >= 75:
#         category = "Good"
#     elif percentage >= 60:
#         category = "Average"
#     else:
#         category = "Poor"
#     return percentage, category
# result = employee(30,27)
# print(result)

# # Sales performance
# def sales(*args):
#     total = 0
#     for i in args:
#         total = total + i
#     if total >= 100000:
#         performance = "Excellent"
#     elif total >= 50000:
#         performance = "Good"
#     elif total >= 25000:
#         performance = "Average"
#     else:
#         performance = "Poor"
#     return total , performance
# result = sales(30000,25000,20000)
# print(result)

# def sales(*args,**kwargs):
#     total = 0
#     for i in args:
#         total = total + i
#     if total >= 100000:
#         performance = "Excellent"
#     elif total >= 50000:
#         performance = "Good"
#     elif total >= 25000:
#         performance = "Average"
#     else:
#         performance = "Poor"
#     return total , performance
# result = sales(30000,25000,20000,name="Yash",department="IT")
# print(result)

# Lambda function
# Question 1
# square = lambda num: num*num
# print(square(7))

# # Question 2
# multiplication = lambda a,b: a*b
# print(multiplication(6,5))

# # Question 3
# num_checker = lambda num : "Positive" if num > 0 else "Negative"
# print(num_checker(-7)) 

# # Question 4
# greater = lambda a,b : a if a > b else b
# print(greater(87,45))  

# # Question 5
# def cube(num):
#     return num*num*num
# numbers = [2,4,6,8,10]
# result = map(cube, numbers)
# print(list(result))
#with lambda
# numbers = [2,4,6,8,10]
# cube = map(lambda num: num*num*num, numbers)
# print(list(cube))

# Question 1
# numbers = [2,4,6,8,10]
# square = map(lambda num:num*num, numbers)
# print(list(square))

# # Question 2
# numbers = [10,20,30,40,50]
# add = map(lambda num:num + 5,numbers)
# print(list(add))

# Question 3
# numbers = [5,10,15,20]
# double = map(lambda num: num*2,numbers)
# print(list(double))

# # Question 5
# marks = [35, 72, 48, 90, 29, 65]
# student = map(lambda marks : "Pass" if marks > 40 else "Fail",marks)
# print(list(student))

# Question 4
# celsius = [0, 10, 20, 30, 40]
# f = map(lambda num: (num*9/5) + 32, celsius)
# print(list(f))

# Filter method
# even number
# numbers = [1,2,3,4,5,6,7,8]
# def even(num):
#     return num % 2 == 0
# result = list(filter(even, numbers))
# print(result)

# # Odd number
# numbers = [10, 15, 20, 25, 30, 35, 40]
# def odd(num):
#     return num % 2 != 0
# result = list(filter(odd,numbers))
# print(result)

# greater than 10
# numbers = [5, 12, 18, 23, 30, 7, 40]
# def greater(num):
#  return num > 10
# result = list(filter(greater, numbers))
# print(result)

# grater than 20 and also even numbers
# numbers = [5, 12, 18, 23, 30, 7, 40, 50, 3]
# def digit(num):
#  return num > 20 and num % 2 == 0
# result = list(filter(digit, numbers))
# print(result)

# filter + lambda
# numbers = [5, 12, 18, 23, 30, 7, 40, 50, 3]
# result = list(filter(lambda num: num > 20 and num % 2 == 0, numbers))
# print(result)

# numbers = [10, 15, 20, 25, 30, 35, 40]
# result = list(filter(lambda num:num % 2 == 0, numbers))
# print(result)

# numbers = [5, 12, 18, 23, 30, 7, 40, 15, 50]
# result = list(filter(lambda num:num % 2 != 0, numbers))
# print(result)

# numbers =  [10, 15, 22, 27, 30, 35, 42, 51, 60]
# result = list(filter(lambda num : num > 30 and num % 2 != 0, numbers))
# print(result)

# soretd () menthod
# # asending order
# numbers = [45, 12, 78, 23, 56, 9, 34]
# result = sorted(numbers)
# print(result)

# Descending order
# numbers = [45, 12, 78, 23, 56, 9, 34]
# result = sorted(numbers, reverse=True)
# print(result)

# alphabetical descending order
# names = ["Yash", "Amit", "Rahul", "Neha", "Kiran"]
# result = sorted(names, reverse=True)
# print(result)

# Sorted + lambda
# student = [("Yash",85),("Amit",92),("Rahul",78),("Neha",90)]
# result = sorted(student, key=lambda x: x[1], reverse=True)
# print(result)

# students = [("Yash", 85),("Amit", 92),("Rahul", 78),("Neha", 90)]
# result = sorted(students, key=lambda x: x[0])
# print(result)

# level 1
# question 1
# numbers = [34, 12, 56, 7, 89, 23]
# result = sorted(numbers)   # asending order
# print(result)

# # question 2
# numbers = [45, 11, 78, 32, 90, 6]
# result = sorted(numbers, reverse=True)   # Descending order
# print(result)

# # Level 2
# # question 3
# names = ["Ravi", "Amit", "Yash", "Neha", "Kiran"]
# result = sorted(names)
# print(result)

# question 4
# names = ["Ravi", "Amit", "Yash", "Neha", "Kiran"]
# result = sorted(names, reverse=True)
# print(result)

# # Level 3
# # question 5
# students = [("Yash", 85),("Amit", 92),("Rahul", 78),("Neha", 90)]
# result = sorted(students, key=lambda x: x[1])
# print(result)

# # question 6
# students = [("Yash", 85),("Amit", 92),("Rahul", 78),("Neha", 90)]
# result = sorted(students, key=lambda x:x[1],reverse=True)
# print(result)

# # Level 4 
# # question 7
# products = [("Laptop", 55000),("Mouse", 800),("Keyboard", 1500),("Monitor", 12000)]
# result = sorted(products, key=lambda x:x[1])
# print(result)

# # question 8
# products = [("Laptop", 55000),("Mouse", 800),("Keyboard", 1500),("Monitor", 12000)]
# result = sorted(products, key=lambda x:x[1],reverse=True)
# print(result)

# # question 9
# names = ["Yash", "Akshay", "Om", "Rahul", "Pranav"]
# result = sorted (names, key=lambda x: len(x))
# print(result)

# Section c
# Question 16
# def is_even(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# result = is_even(7)
# print(result)

# # Question 17
# def sum_numbers(*args):
#     total = 0
#     for i in args:
#         total = total + i
#     return total
# result = sum_numbers(10, 20, 30)
# print(result)

# # Question 18
# numbers = [2, 4, 6, 8, 10]
# result = map(lambda num: num*num, numbers)
# print(list(result))

# # Question 19
# numbers = [5, 12, 18, 23, 30, 7, 40, 15, 50]
# result = filter(lambda num: num > 20 and num % 2 == 0,numbers)
# print(list(result))

# # Question 20
# students = [("Yash", 85),("Amit", 92),("Rahul", 78),("Neha", 90)]
# result = sorted(students, key=lambda x:x[1] , reverse=True )
# print(list(result))

# Recursion
# def print_num(n):
#     if n == 0:     # base case
#         return
#     print(n)
#     print_num(n - 1)   # recursive call
# print_num(10)

# question 2
# def sum_num(n):
#     if n == 0:
#          return 0
#     return n + sum_num(n - 1)
# print(sum_num(5))

# def  print_num(n):
#     if n == 0:
#         return
#     print(n)
#     print_num(n - 1)
# print_num(5)

# def print_num(n):
#     if n == 0:
#         return
#     print_num(n - 1)
#     print(n)
# print_num(10)

# def sum_num(n):
#     if n == 0:
#         return 0
    
#     return n + sum_num(n - 1)
# print(sum_num(4))

# def fact(n):
#     if n == 0:
#         return 1
#     return n*fact(n - 1)
# print(fact(5))

# def digit_sum(n):
#     if n == 0:
#         return 0
#     digit = n % 10
#     return digit + digit_sum(n // 10)
# print(digit_sum(1234))

# def reverse_num(n, reverse):
#     if n == 0:
#         return reverse
#     digit = n % 10
#     reverse = reverse*10 + digit
#     return reverse_num(n // 10, reverse)
# print(reverse_num(6789, 0))

# def print_num(n):
#     if n == 0:
#         return
#     return n + print_num(n // 10)
# print(print_num(1234))

# def fact(n):
#     if n == 0:
#         return 1
#     return n* fact(n - 1)
# print(fact(5))

# def print_num(n):
#     if n == 0:
#         return
#     print(n)
#     print_num(n - 1)
# print_num(5)

# def count_digit(n):
#     if n == 0:
#         return 0
#     digit = n % 10
#     return 1 + count_digit(n // 10)
# print(count_digit(12345))

# def digit_sum(n):
#     if n == 0:
#         return 0
#     digit = n % 10
#     return digit + digit_sum(n // 10)
# print(digit_sum(12345))

 # string + recursion
# def palindrome(s):
#     if len(s) <= 1:
#         return  "Palindrome"
#     if s[0] != s[-1]:
#         return  "Not palindrome"
#     return palindrome (s[1 :-1])
# print(palindrome("hello"))

# def print_char(s):
#     if s == "":
#         return 0
#     if s[0].lower() == "g":
#         return 1 + print_char(s[1:])
#     return print_char(s[1:])
# print(print_char("Programming"))

# # String
# # question 1
# name = "Python"
# print(name[0])
# print(name[2])
# print(name[5])
# print(len(name))

# # question 2
# word = "Programming"
# print(word[0])
# print(word[10])
# print(word[1])
# print(word[-2])

# name = "  akshada bhosale  "
# print(name.strip().title())

# text = "I like java"
# print(text.replace("java","python").upper())

# text = "python java python c python"
# print(text.count("python"))

# username = "Akshada123"
# print(username.isalnum())

# text = "python is very easy"
# print(text.find("python"))

# email = "akshada@gmail.com"
# print(email.startswith("akshada"))
# print(email.endswith("com"))

# text = "  I LIKE PYTHON   "
# print(text.strip().replace("PYTHON","JAVA").lower())

# sentense = "Python is very easy"
# print(sentense.split())
# print(len(sentense.split()))

# text = "12345"
# print(text.isalpha())
# print(text.isdigit())

# Problem 1  indexing
# text = "python"
# print(text[0])
# print(text[2])
# print(text[5])

# # Problem 2  slicing
# text = "programming"
# print(text[0:3])

# # Problem 3  
# text = "programming"
# print(text[7:])

# # Problem 4
# text = "python"
# print(text[: :-1])

# # Problem 5
# text = "python programming"
# print(text.upper())

# # Program 6
# text = "I like java"
# print(text.replace("java","python"))

# # Problem 7
# text = "banana"
# print(text.count("a"))

# # Problem 8
# text = "i love python"
# print(text.find("python"))

# # Problem 9
# text = "python123"
# print(text.isalnum())

# # Problem 10
# text = "  python programming  "
# print(text.strip().title())

























    