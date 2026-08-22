# Employee information system
# ---------Employee detail--------------
"""Emp_name = input("Enter Emp name:")   #employee name
Emp_ID =input("Enter Emp ID:")        #employee ID
department = input("Enter Emp department:") #emp department
salary = float(input("Enter Emp salary:"))   #emp salary
print("/n-----employee details-----")
print("Employee name:",Emp_name)
print("Employee ID:",Emp_ID)
print("Department:",department)
print("salary:",salary)"""

#Student percentage calculator
"""python=int(input("Enter marks of python = "))    #98
java =int(input("Enter marks of java = "))       #90
javascript =int(input("Enter marks of javascript = "))   #85
html =int(input("Enter marks of html = "))             #92
css =int(input("Enter marks of css = "))                 #80
Total = python + java + javascript + html + css    #output = 5
percentage = Total / 5     
print("Total=",Total)
print("Percentage:",percentage,"%")  """

#Product bill generator
"""name=input("Enter product Name:")
price=float(input("Enter product price:"))
quantity=float(input("Enter product quantity:"))
Total=price*quantity
print("/n------Product Details------")
print("Product Name:",name)
print("Product price:",price)
print("Product quantity:",quantity)
print("Total Bill:",Total)"""

#Temperature Converter
"""temperature = float(input("Enter temperature in celcius = "))
fahrenheit = (temperature*9/5)+32
print("Temparature in fahrenheit=",fahrenheit)"""

#Age calculator
"""Birth_year=int(input("Enter you birth year = "))
current_year=int(input("Enter current year = "))

Age = current_year - Birth_year
print("Birth year =",Birth_year)
print("current year =",current_year)
print("Your age is =",Age)"""

#Login system
"""stored_username="Admin"
stored_password="1234"

username=input("Enter username:")
password=input("Enter password:")

print("condition:",username == stored_username and password == stored_password)

if username == stored_username and password == stored_password:
    print("Login successful !")
else:
    print("Invalid username and password")"""

# DataType Checker
"""Name = input("Enter your name:")
Age = int(input("Enter your age:"))
Height = float(input("Enter your height:"))
salary = float(input("Enter your salary:"))
print(type(Name))
print(type(Age))
print(type(Height))
print(type(salary))"""

#Type casting program
"""num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
print("sum = ",num1+num2)"""

#Electricity bill calculator
"""Unit = int(input("Enter units:"))
rate =input("Enter rate : 8")
Total_bill= Unit*8
print("Bill =",Total_bill)"""

#Company registration form
#Company details
"""Name = input("Enter Company Name:")
#Employee details
Emp_name =input("Enter Employee Name:")
Emp_ID =int(input("Enter Employee ID:"))
designation =input("Enter Emp designation:")
salary =int(input("Enter Emp salary:"))

print("/n-----Details-------")
print("Company Name : ",Name)
print("Employee Name : ",Emp_name)
print("Employee ID : ",Emp_ID)
print("Designation : ",designation)
print("salary : ",salary)"""

#Mini ATM
"""name = input("Enter your name:")
acc_number=int(input("Enter account number:"))
balance =int(input("Enter current balance:"))
withdraw =int(input("Enter withdraw amonunt:"))
remaining_balance=balance - withdraw
if withdraw > balance :
    print("Insufficient balance")
else:
    print("Transaction successful !")
    print("Remaining Balance : ",remaining_balance)"""

#Salary increment calculator
"""name =input("Enter your name:")
current_salary = int(input("Enter current salary:"))
increment = current_salary*15/100     # 15% increment
new_salary = current_salary+increment  
print("Name:", name)
print("Current salary:", current_salary)
print("New salary :",new_salary)"""

#Shopping discount calculator
"""Name = input("Enter product name:")
price = int(input("Enter product price:"))
Discount = int(input("Enter discount:",))
discount_amount = price*Discount/100    #discount amount
Final_amount = price - discount_amount   #final amount
print("/n------Final Bill-------")
print("Discount Amount:",discount_amount)
print("Final Amount :", Final_amount)"""

#Rectangle Calculator
"""length = float(input("Enter a length ="))
width = float(input("Enter a width ="))
Area = length*width                                #Area
perimeter =2*(length + width)                    #perimeter
print("Area of rectangle =",Area)
print("perimeter of rectangle =",perimeter)"""

#Circle calculator
"""length =float(input("Enter length of circle:"))
width =float(input("Enter width of circle:"))
radius = float(input("Enter a radius of circle:"))
Diameter = 2*radius                 #Diameter=2*r
circumference=2*3.14*radius         #c=2*3.14*r
Area = length*width                 #Area=L*W
print("Diameter of circle:",Diameter)
print("circumference of circle:",circumference)
print("Area of circle:",Area)"""

#Average speed calculator
"""Distance =float(input("Enter a distance(km) ="))
Time =float(input("Enter a time(hour)"))
speed = Distance/Time                   #speed formula
print("Speed =", speed)"""

#BMI calculator
"""weigth = float(input("Enter your weight ="))
height = float(input("Enter your height ="))
BMI = weigth/(height*height)          #BMI formula
print("BMI =", BMI)"""

#Marks Grade Calculator
"""Math = int(input("Enter marks of math ="))
english = int(input("Enter marks of english ="))
physics = int(input("Enter marks of physics ="))
chemistry = int(input("Enter marks of chemistry ="))
history = int(input("Enter marks of history ="))
Total = Math+english+physics+chemistry+history
percentage = Total/5
print("percentage =",percentage,"%")"""

#Swap Two Numbers
"""num1 = int(input("Enter first number ="))
num2 = int(input("Enter second number ="))
temp = num1
num1 = num2
num2 = num1
print("/nAfter swapping:")
print("First number is:", num1)
print("Second number is:", num2)"""

#Company ID generator
"""name = input("Enter employee name:")
code = input("Enter department code :")
year =input("Enter joining year :")
ID = code+year
print("Company ID :", ID)"""

#Mini Bank Balance
"""name = input("Enter a name :")
balance = int(input("Enter current balance :"))
deposite = int(input("Enter deposite amount :"))
New_balance = balance+deposite
print("initial balance :",balance)
print("deposite :",deposite)
print("New balance :", New_balance)"""

#Student Result System
"""Name = input("Enter student name =")
Roll_no = int(input("Enter roll no ="))
physics = int(input("Enter marks of physics ="))
chemistry = int(input("Enter marks of chemistry ="))
math = int(input("Enter marks of math ="))
english = int(input("Enter marks of english ="))
python = int(input("Enter marks of python ="))
Total = physics + chemistry + math + english + python
percentage = Total/5
Avg = Total/5
print("-------Student result--------")
print("Student name =", Name)
print("Roll no =", Roll_no)
print("Total =",Total)
print("Percentage =",percentage)
print("Average =",Avg)"""

#Interview level program

#ATM transaction
"""stored_PIN =1624
Balance =int(input("Enter initial balance ="))
Transfer =int(input("Enter transfer amount ="))
Pin =int(input("Enter Account pin ="))
print("Condition =",Balance >= Transfer and stored_PIN == Pin)
if Balance >= Transfer and stored_PIN == Pin :
    print("Transaction successful !")
    Final_balance = Balance - Transfer
    print("After transfer your remaining account balance is ",Final_balance)
else:
    print("Transaction failed !")"""

"""#Shopping Bill
#product details
product_1 =float(input("Enter product1 price ="))
product_2 =float(input("Enter product2 price ="))
product_3 =float(input("Enter product3 price ="))
product_4 =float(input("Enter product4 price ="))
product_5 =float(input("Enter product5 price ="))
Total = product_1+product_2 +product_3 + product_4 + product_5
                                         #sum of total product
GST = Total*0.18                  # GST amount
Final_bill = Total + GST          # final bill
print("------Final bill-------")
print("Total price of products =", Total) 
print("GST amount =",GST)
print("Final Bill =",Final_bill)         #final output"""

# Time Converter
"""minute =int(input("Enter minutes ="))
hours = minute // 60
remaining_minute = minute % 60
print("Hours =",hours)
print("Remaining minutes =",remaining_minute)"""

#Bill Splitting Calculator
"""total_bill = int(input("Enter total bill ="))
persons = int(input("Enter number of persons ="))
service_charge = total_bill*0.05     # SC =5%
final_bill = total_bill + service_charge
per_person_bill = final_bill / persons
print("------Bill Details-------")
print("Total bill =", total_bill)
print("Number of persons =", persons)
print("Service charge =", service_charge)
print("Final bill =", final_bill)
print("Per person bill =", per_person_bill)"""

# Distance converter
"""kilometer =int(input("Enter kilometer :"))
# km convert in meter,cm and mile
meter = kilometer*1000
centimeter = kilometer*100000
mile = kilometer/1.60934
print("Meter is =",meter)
print("centimeter is =",centimeter)
print("mile =",mile)"""

# Marks Analyzer
# subjects
"""physics = int(input("Enter marks of physics ="))
maths = int(input("Enter marks of maths ="))
chemistry = int(input("Enter marks of chemistry ="))
english = int(input("Enter marks of english ="))
python = int(input("Enter marks of python ="))
# Total
total = physics + maths + chemistry + english + python
# Percentage
percentage = total  /5
# Average
average = total / 5
# Highest 
highest = physics
if maths > highest:
  highest = maths
if chemistry > highest:
  highest = chemistry
if english > highest:
  highest = english
if python > highest:
  highest = python
# Lowest
lowest = physics
if maths < lowest:
  lowest = maths
if chemistry < lowest:
  lowest = chemistry
if english < lowest:
  lowest = english
if python < lowest:
  lowest = python
# Output
print("Total =",total)
print("Percentage =",percentage, "%")
print("Average =", average)
print("Highest marks =",highest)
print("Lowest marks =",lowest)"""

# Cash Breakdown
"""amount = int(input("Enter withdrawal amount ="))
notes_500 = amount // 500
remaining = amount % 500
notes_200 = remaining // 200
remaining = remaining % 200
notes_100 = remaining // 100
remaining = remaining % 100
notes_50 = remaining // 50
remaining = remaining % 50
notes_10 = remaining // 10
remaining = remaining % 10
print("------Cash Breakdown------")
print("500 Notes =",notes_500)
print("200 Notes =",notes_200)
print("100 Notes =",notes_100)
print("50 Notes =",notes_50)
print("10 Notes =",notes_10)
print("Remaining Amount =",remaining)"""

#Monthly budget calculator
"""income = int(input("Enter monthly income ="))
food_expense =int(input("Enter food expense ="))
travel_expense =int(input("Enter travel expense ="))
shopping_expense =int(input("Enter shopping expense ="))
rent =int(input("Enter monthly rent ="))
other_expense =int(input("Enter other expense ="))
total_expense = food_expense+travel_expense+shopping_expense+rent+other_expense
remaining = income - total_expense
percentage = (remaining/income)*100
print("------Total monthly budget-------")
print("Monthly income =",income)
print("Total expense =",total_expense)
print("Remaining money =",remaining )
print("saving percentage =",percentage,"%")"""

# Electricity bill calculator
"""units = int(input("Enter units ="))
if units <= 100:
    bill = units*5
elif units <= 200:
    bill = (units*5) + (units - 100)*7
else :
    bill = (units*5)+(units*7)+(units - 200)*10
print("------ Electricity bill------")
print("Units =", units)
print("Total bill =",bill)"""

#ATM withdrawal
#stored pin
"""stored_pin =1624
#Input
balance = int(input("Enter initial balance :"))
withdraw = int(input("Enter withdraw amount :"))
PIN = int(input("Enter ATM pin :"))
remaining = balance - withdraw
#condition
print("Condition :", balance >= withdraw and withdraw % 500 ==0 and PIN == stored_pin )
if balance >= withdraw and withdraw % 500 ==0 and PIN == stored_pin:
    print("Transaction successful !")
    print("Remaining balance :",remaining)
else :
     print("Transaction failed :")"""

# Movie ticket booking
# Input
"""age =int(input("Enter age :"))
ticket =int(input("Enter number of ticket :"))
#Logic
if age <= 5 :
    ticket_price = 0
elif age <= 18:
    ticket_price = 100
else:
    ticket_price = 200
total_amount = ticket_price * ticket
# Output
print("------Movie ticket------")
print("Age =",age)
print("Number of tickets =",ticket)
print("Ticket price =",ticket_price)
print("Total amount =",total_amount)"""

"""#Salary calculator
salary =int(input("Enter basic salary ="))  #Input
#Logic
if salary <= 20000:
    bonus =salary*10 / 100
elif salary >= 20000 and salary <= 50000:
    bonus =salary*15 /100
else:
    salary >= 50000
    bonus = salary*20 /100
total = bonus + salary
# output
print("-----Final salary------")
print("Your basic salary =",salary)
print("Bonus =",bonus)
print("Total salary =",total)"""

"""#Shopping discount calculator
#Input
amount = int(input("Enter shopping amount :"))
#Conditions
if amount <= 5000:
    discount_amount = amount*0 /100
elif amount <= 10000:
    discount_amount = amount*10/100
else :
    amount >= 10000
    discount_amount = amount*20/100
# after added discount and shopping amount
final_bill = amount - discount_amount   
print("------Final Bill------")
print("Shopping amount =",amount)
print("Discount amount =",discount_amount)
print("Final bill =",final_bill)"""

"""#Grade calculator
# Input
marks = int(input("Enter marks : "))
# Conditions
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else :
    grade = "Fail"
# Output
print("Your grade is :",grade)"""

"""# Logic system
# Stored value
stored_username ="Akshada"
stored_password = 1624
#Input
username = input("Enter username :")
password = int(input("Enter password :"))
# Conditions
if username == stored_username and password == stored_password:
    print("Login successful !")
elif username != stored_username :
    print("Invalid username")
else:
    print("Invalid password") """

"""# ATM security system
# stored pin
stored_PIN ="1624"
#Input
balance = int(input("Enter account balance :"))
pin =input("Enter account pin :")
withdraw =int(input("Enter withdraw amount :"))
remaining = balance - withdraw
# conditions
if pin != stored_PIN:
    print("Invalid pin")
elif  withdraw > balance:
    print("Insufficient balance")
elif  withdraw % 500 != 0:
    print("Invalid amount")
else:
    print("Transaction successful !")
    print("Remaining balance :", remaining)"""

"""#Online shopping payment system
# coupon code
stored_code ="SAVE10"
# Input
balance = int(input("Enter account balance ="))
amount = int(input("Enter shopping amount ="))
code =input("Enter coupon code =")
# check discount
if stored_code == code:
    discount = amount*10/100
else:
    discount = 0
# final amount
final_amount = amount - discount
# Payment
if balance >= final_amount:
    print("Payment successful !")
else:
    print("Insufficient balance")
# Remaining
remaining = balance - final_amount
print("------Final Bill------")
print("Account balance =",balance)
print("Shopping amount =",amount)
print("Coupon code =",code)
print("Discount =",discount)
print("Final bill =",final_amount)
print("Remaining balance =",remaining)"""

"""# Student scholarship elligibility
# Input
marks =float(input("Enter your marks :"))
income = int(input("Enter family income:"))
attendance =int(input("Enter your attendance :"))
# Logic
if marks < 75:
    print("Scholarship rejected - marks")
elif income > 300000:
    print("Scholarship rejected - income")
elif attendance < 75:
    print("Scholarship rejected - attendance")
else:
    print("Scholarship approved !")"""

"""# Bank loan elligibility
# Input
age = int(input("Enter your age :"))
salary = int(input("Enter your salary :"))
credit_score = int(input("Enter credit score :"))
# Conditions
if age < 21:
    print("Loan rejected - Age")
elif salary < 25000:
    print("Loan rejected - Salary")
elif credit_score < 700:
    print("Loan rejected - Credit score")
else:
    print("Loan approved !")"""












