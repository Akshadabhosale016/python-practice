# If statement

"""# Print positive number
number = int(input("Enter number :"))
if number > 0:
    print("Positive number") """

"""#Print Even number
num = int(input("Enter a number:"))
if num % 2==0:
    print("Even number")"""

"""# eligibility
name = input("Enter your name :")
age = int(input("Enter your age:"))
if age >= 18 :
    print(name,"you are elligible to vote")"""

"""# Discount
amount = int(input("Enter shopping amount :"))
if amount > 5000:
    discount = amount*10 / 100 
    final_amount = amount - discount
    print("-----Final Bill-----")
    print("Discount :",discount)
    print("Total :", final_amount)"""

"""# Temperature
temperature = int(input("Enter temperature :"))
if temperature > 30 :
    print("It's a hot day")"""

"""# Marks
marks = int(input("Enter your marks:"))
if marks >= 40 :
    print("Pass")"""

"""num = int(input("Enter a number :"))
if num > 10 and num < 50:
    print("Number is between 10 and 50")"""

# If else statement
"""# check enen or odd
num = int(input("Enter a number:"))
# condittion
if num%2 ==0:
    print(num,"is Even number")
else:
    print(num,"is Odd number")"""

"""# check num is positive,negative or zero
num = int(input("Enter a number :"))
# condition
if num > 0:
    print(num,"is Positive number")
elif num < 0:
    print(num,"is Negative number")
else:
    print(num,"is Zero")"""

"""# Greater number
num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
num3 = int(input("Enter third number :"))
# condition
if num1 > num2 and num1 > num3:
    print(num1,"is Greater number")
elif num2 > num1 and num2 > num3:
    print(num2,"is Greater number")
elif num3 > num1 and num3 > num2:
    print(num3,"is Greater number")
else:
    print("some number are both equal")"""

"""# pass or fail
name = input("Enter student name :")
marks = int(input("Enter student marks :"))
# conditions
if marks >= 40 :
    print(name,"is Pass")
else :
    print(name,"is Fail")"""

"""# print grade according marks
marks = int(input("Enter a marks :"))
# condition
if marks >= 85 :
    print("A")
elif marks >= 70:
    print ("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")"""

"""# check elligibility to driving license
name = input("Enter your name =")
age = int(input("Enter your age ="))
# condition
if age >= 18 :
    print(name,"is elligible to driving license")
else:
    print(name,"is NOT elligible to driving license")"""

"""# Divisible by 3 and 5
num = int(input("Enter a number ="))
#condition
if num%3==0 and num%5==0:
    print(num,"is divisible by 3 and 5")
else:
    print(num,"is NOT divisible by 3 and 5")"""

"""# check leap year
year = int(input("Enter year :"))
# condition
if year%400==0 or (year%4==0 and year%100 != 0):
    print(year,"is leap year")
else:
    print(year,"is NOT leap year")"""

"""# check username and password
stored_username = "Akshada"
stored_password = 1617
# Input
username =input("Enter username =")
password =int(input("Enter password ="))
# condition
if stored_username == username and stored_password == password:
    print("Login successful !")
else :
    print("Invalid username and password")"""

"""# Electricity bill calculate
units = int(input("Enter units :"))
# condition
if units <= 100:
    rate = 5
elif units <= 200:
    rate = 7
else:
    rate = 10
total_bill = units*rate
print("------Electricity Bill------")
print("Units =",units)
print("Rate =",rate)
print("Electricity bill =",total_bill)"""

"""# simple calculator
# Input
num1 = float(input("Enter first number ="))
operator = input("Enter operator (+, -, *, /) :")
num2 = float(input("Enter second number ="))
# condition
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Invalid operator")
    result = None
if result is not None:
    print("Result =", result)"""

"""# Check vowel and consonant
ch = (input("Enter a alphabet :")).lower()
# conditions
if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
   print(ch,"is vowel")
else:
   print(ch,"is consonant ")"""

"""# check character alphabet, digit and special character
ch = input("Enter a character :").lower()
# condition
if ch.isalpha():
    print(ch,"is a alphabet")
elif ch.isdigit():
    print(ch,"is a digit")
else:
    print(ch,"is a special character")"""

"""# calculate amount
amount = int(input("Enter purchase amount :"))
# Condition
if amount >= 5000:
    discount = amount*20/100
elif amount >= 3000:
    discount = amount*10/100
elif amount >= 1000:
    discount = amount*5/100
else:
    discount = 0
final_amount = amount - discount
print("------Final Bill------")
print("Purchase amount =",amount)
print("Discount =",discount)
print("Total Bill =",final_amount)"""

"""#ATM withdrawal condition
# user input
balance = int(input("Enter account balance ="))
withdraw = int(input("Enter withdraw amount ="))
# condition
if withdraw <= 0 :
    print("Invalid withdraw amount")
elif withdraw > balance :
    print("Insufficient balance")
elif withdraw % 500 != 0:
    print("please, Enter amount multiple of 500")
else:
    reamining = balance - withdraw
    print("------Final Bill-------")
    print("Initial balance =", balance)
    print("Withdraw amount =",withdraw)
    print("Reamining balance =",reamining)"""

"""# Student result system
name = input("Enter student name :")
biology = int(input("Enter biology marks ="))
chemistry = int(input("Enter chemistry marks ="))
physics = int(input("Enter physics marks ="))
total = biology + chemistry + physics
percentage = total / 3
# conditions
if biology < 40 or chemistry < 40 or physics < 40:
    print (name,"is fail")
else:
    print("Total =",total)
    print("Percentage =",percentage,"%")
    if percentage >= 75:
      print("Distinction")
    elif percentage >= 60:
       print("First class")
    elif percentage >= 50:
      print("Second class")
    else:
       print("Pass")"""

# Nested if statement

'''# Age category
age = int(input("Enter your age ="))
# Condition
if age < 0:
    print("Invalid age")
elif age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior citizen")'''

'''# Electricity bill - slab calculation
units = int(input("Enter a units ="))
# conditions
if units <= 0:
    print("Invalid units")
elif units <= 100:
    rate = 5
elif units <= 200:
    rate = 7
elif units <= 300:
    rate = 10
else:
    rate = 12   
if units > 0:
    total = units*rate
    print("------Final Bill------")
    print("Units =",units)
    print("Rate =",rate)
    print("Total Bill =",total)'''

'''# ATM pin verification
# stored pin
correct_pin = 1234
# user input
pin = int(input("Enter PIN :"))
balance = int(input("Enter account balance :"))
withdraw = int(input("Enter withdraw amount :"))
# Condition
if correct_pin != pin:
    print("Invalid PIN")
elif withdraw <= 0:
    print("Invalid amount")
elif withdraw > balance:
    print("Insufficient balance")
elif withdraw % 500 != 0:
    print("please enter amount in multiple of 500")
else:
    print("withdrawal successful !")
    remaining = balance - withdraw 
    print("---- OUTPUT------")
    print("Initial balance =",balance)
    print("Withdraw amount =",withdraw)
    print("Remaining amount =",remaining)'''

'''# Login system
# stored username and password
stored_username = "Akshada"
stored_password = 1624
# user input
username = input("Enter username =")
password = int(input("Enter password ="))
# Conditions
if stored_username == username:
    if stored_password == password:
        print("Login successful !")
        print("Welcome",username)
    else:
        print("Invalid password")
else:
    print("Invalid username")'''

'''# Online shopping payment system
amount = int(input("Enter amount ="))
payment_method = (input("Enter method(Card, UPI, Cash) ="))
# conditions
if amount <= 0:
    print("Invalid amount")
else:
    if payment_method =="Card":
        print("Card payment successful !")
    elif payment_method == "UPI":
        print("UPI payment successful !")
    elif payment_method == "Cash":
        print("Cash payment selected !")
    else:
        print("Invalid payment method")'''

'''# Number checker
# user input
num = int(input("Enter a number ="))
# condition
if num > 0:
    print(num,"is Positive")
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
elif num < 0:
    print(num," is Negative")
else:
    print("Zero")'''

'''# electricity bill with discount
unit = int(input("Enter units :"))
# condition
if unit <= 0:
    print("Invalid unit")
elif unit <= 100:
    rate = 5
elif unit <= 200:
    rate = 7
else:
    rate = 10
if unit >= 0:
    total = unit*rate
    if total > 2000:
        discount = total*10 /100
    else:
        discount = 0
    final_bill = total - discount
    print("-----Final Bill-----")
    print("Units =",unit)
    print("Rate =",rate)
    print("Total =",total)
    print("Discount =",discount)
    print("with discount final Bill =",final_bill)'''

'''# Movie ticket booking
age = int(input("Enter age :"))
price = int(input("Enter ticket price :"))
no_ticket = int(input("Enter number of ticket :"))
# conditions
if age <= 0:
    print("Invalid age")
elif no_ticket <= 0:
    print("Invalid number of ticket")
else:
    total = price*no_ticket
    if age <= 12:
        discount = total*50 / 100
    elif age >= 60:
        discount = total*30 / 100
    else:
        discount = 0
final = total - discount
print("---Final Bill---")
print("Age :",age)
print("Price :",price)
print("Number of ticket :",no_ticket)
print("Amount :",total)
print("Discount :",discount)
print("Final amount :",final)'''

'''# ATM withdrawal system with nested if statement
stored_pin = 1624
balance = int(input("Enter Account balance ="))
withdraw = int(input("Enter withdraw amount ="))
pin = int(input("Enter pin ="))
# Condition
if pin != stored_pin:
    print("Invalid PIN")
elif withdraw <= 0:
    print("Invalid amount")
elif withdraw > balance:
    print("Insufficient balance")
elif withdraw%500 != 0:
    print("enter amount muptiple of 500")
else:
    print("withdraw successful !")
    remaining = balance - withdraw
    print("PIN =",pin)
    print("Initial balance =",balance)
    print("Withdraw =",withdraw)
    print("Remaining balance =",remaining )'''

'''# student result + grade system
name = input("Enter student name =")
physics = int(input("Enter physics marks ="))
chemistry = int(input("Enter chemistry marks ="))
biology = int(input("Enter biology marks ="))
total = physics + chemistry + biology
percentage = total/3
# condition
if physics < 40 or chemistry < 40 or biology < 40:
    print(name,"is fail")
else:
    print("Total =",total)
    print("Percentage =",percentage,"%")
    if percentage >= 75:
        print("Distinction")
    elif percentage >= 60:
        print("First class")
    elif percentage >= 50:
        print("Second class")
    else:
        print("Pass")'''

'''# Age + Category + Elligibility system
name = input("Enter your name =")
age = int(input("Enter your age ="))
# condition
if age < 0:
    print("Invalid age")
else: 
    if age <= 12:
     print("Child")
    elif age <= 19:
     print("Teenager")
    elif age <= 60:
     print("Adult")
    else:
     print("Senior citizen")
    if age >= 18:
        print(name,"you are elligible for driving license")
    else:
        print(name,"you are NOT elligible for driving license")'''

'''# shopping discount system
name = input("Enter a name =")
amount = int(input("Enter shopping amount ="))
membership = input("Enter membership (YES, NO) =")
# condition
if amount <= 0:
    print("Invalid amount")
else:
    if amount >= 5000:
           discount = amount*20 /100
    elif amount >= 3000:
         discount = amount*10 /100
    elif amount >= 1000:
         discount = amount*5 / 100
    else:
         discount = 0
    after_discount = amount - discount
    if membership == "YES" :
        extra = after_discount*5/100
    else:
        extra = 0
    final = after_discount - extra
    print("Extra discount =",extra)
    print("----Final Bill----")
    print("Customer Name :",name)
    print("Amount :",amount)
    print("Discount :",discount)
    print("Extra membership discount :",extra)
    print("Final amount :",final)'''

'''# ATM transaction system
# ATM with PIN + Balance + withdrawal
stored_pin = 1624
balance = int(input("Enter Initial balance ="))
withdraw = int(input("Enter withdraw amount ="))
pin = int(input("Enter account PIN ="))
# conditions
if stored_pin != pin:
    print("Invalid PIN")
else:
    if withdraw <= 0:
           print("Invalid amount")
    elif withdraw > balance:
         print("Insufficient balance")
    elif withdraw%500 != 0:
         print("Please,Enter amount multiply of 500")
    else:
         remaining = balance - withdraw
         print("Withdrawal Successeful ! ")
         print("Initial balance =",balance)
         print("withdraw amount =",withdraw)
         print("Remaining balance =",remaining)'''

'''# Electiricity Bill + Discount
name = input("Enter name :")
unit = int(input("Enter units :"))
# conditions
if unit <= 0:
    print("Invalid units")
else:
    if unit <= 100:
           rate = 5
    elif unit <= 200:
           rate = 7
    elif unit <= 300:
           rate = 10
    else:
           rate = 12
    bill = unit*rate
    if bill >= 3000:
                discount = bill*10 / 100
    else:
                discount = 0  
    final = bill - discount  
    print("-----Electricity bill-----")
    print("Units =", unit)
    print("Rate =",rate) 
    print("Bill =",bill)
    print("Discount =",discount)
    print("Final bill  after discount = ",final) '''

'''# Salary + Bonus calculations
name =input("Enter name :")
salary =int(input("Enter salary :"))
experience = int(input("Enter working experience(years) :"))  
if salary <= 20000:
    bonus = salary*5 / 100
elif salary <= 50000:
    bonus = salary*10 / 100
else:
    bonus = salary*15 / 100
    
if experience > 5:
    extra_bonus = bonus*5 / 100
else:
    extra_bonus = 0
total = bonus + extra_bonus
final_salary = salary + total
print("-----Final salary------")
print("Name =",name)
print("Initial Salary =",salary)
print("Experience =",experience)
print("Bonus according to salary =",bonus)
print("with bonus =",total)
print("with extra bonus =",final_salary)'''

'''# Bank loan elligibility system
name = input("Enter name :")
age = int(input("Enter age :"))
salary = int(input("Enter salary :"))
score = int(input("Enter credit score :"))
# conditions
if age < 18 or age > 60:
    print("Not elligible")
elif salary < 20000:
    print("Not elligible")
else:
     if score >= 700:
         print(name,"your loan approved !") 
     else:
         print(name,"your loan rejected !")'''

'''# Restaurant bill + Discount
name = input("Enter name =")
bill = int(input("Enter restaurant bill ="))
membership = input("Enter membership(Yes / No) =")
# condition
if bill >= 5000:
    discount = bill*20 / 100
elif bill >= 3000:
    discount = bill*10 / 100
elif bill >= 1000:
    discount = bill*5 / 100
else:
    discount = 0
    total_bill = bill - discount
    if membership == 'Yes':
        extra_discount = total_bill*5 / 100
    else:
        extra_discount = 0
    final_bill = total_bill - extra_discount
print("-----Result-----")
print("Your name =",name)
print("starting bill =",bill)
print("discount bill =",total_bill)
print("Extra discount bill =",final_bill)'''

'''# E-Commerce order system
name = input("Enter customer name =")
amount = int(input("Enter amount ="))
membership = input("Do you have membership ? (Yes/No) =")
delivery = input ("How you want delivery ? (Express/Normal) =")
# conditions
if amount >= 5000:
    discount = amount*20/100
elif amount >= 3000:
    discount = amount*10/100
elif amount >= 1000:
    discount = amount*5/100
else:
    discount = 0
discount_amount = amount - discount
# membership
if membership == "Yes":
    membership_discount = discount_amount*5/100
else:
    membership_discount = 0
# Delivery
if delivery == "Express":
    delivery_charge = 200
else:
    delivery_charge = 50
total_amount = discount_amount - membership_discount + delivery_charge
print("-----Bill Details-----")
print("Customer name =",name)
print("Amount =",amount)
print("Membership =",membership)
print("Delivery =",delivery)
print("Discount =",discount)
print("After discount =",discount_amount)
print("After membership discount =",membership_discount)
print("Delivery charge =",delivery_charge)
print("Total =",total_amount)'''

'''# Employee Bonus Calculator
name = input("Enter name =")
salary = int(input("Enter current salary ="))
experience = int(input("Enter experience (0-50) ="))
performance = input("Enter performance (Excellent/Good/Average)=")
#condition
if experience >= 5 and performance == "Excellent":
    bonus = salary*20/100
elif experience >= 5 and performance == "Good":
    bonus = salary*15/100
elif experience < 5 and performance == "Excellent":
    bonus = salary*10/100
else:
    bonus = salary*5/100
total_salary = salary + bonus
print("Name =",name)
print("Salary =",salary)
print("Experience =",experience)
print("Performance =",performance)
print("Bonus =",bonus)
print("After bonus =",total_salary)'''

'''# scholarship elligibility
name = input("Enter your name :")
marks = int(input("Enter your marks :"))
attendance = int(input("Enter attendance :"))
income = int(input("Enter income :"))
#Condition
if marks >= 85 :
    if attendance >= 90 and income <= 500000:
        scholarship = 50
        status ="Eligible"
    else:
        scholarship = 30
        status = "Eligible"

elif marks >= 70 :
    if attendance >= 85 and income <= 300000:
        scholarship = 25
        status = "Eligible"
    else:
        scholarship = 0
        status = "Not eligible"
else:
 scholarship = 0
status = "Not eligible"
print("-----Scholarship Eligibility-----")
print("Name =",name)
print("Marks =",marks)
print("Attendance =",attendance)
print("Income =",income)
print("Scholarship =",scholarship,"%")
print("Status =",status)'''






              


    
 

    



        
    

            





    
        
        





    
    



   





 


    
