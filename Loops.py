#print 1 to n numbers using while loop
# n =int(input("Enter a number :"))
# i = 1
# while i <= n:
#     print(i)
#     i += 1

#print n to 1 numbers using while loop
# n = int(input("Enter a number :"))
# i = n
# while i >= 1:
#     print(i)
#     i -= 1

# print even number 1 to n
# n = int(input("Enter number :"))
# i = 1
# while i <= n:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# print odd numbers
# n = int(input("Enter a number ="))
# i = 1
# while i <= n:
#     if i % 2 != 0:
#         print(i)
#     i += 1

# print number of sum
# num = int(input("Enter a number ="))
# i = 1
# total = 0
# while i <= num:
#     total = total + i
#     i += 1
# print("Sum =",total)

# print sum of even number
# num = int(input("Enter a number :"))
# i = 1
# total = 0
# while i <= num:
#     if i % 2 == 0:
#         total = total + i
#     i += 1
# print("Sum of Even number =",total)

# print sum of odd number
# num = int(input("Enter number ="))
# i = 1
# total = 0
# while i <= num:
#     if i % 2 != 0:
#         total = total + i
#     i += 1
# print("Sum of odd number =",total)

# print multiplication table
# n = int(input("Enter number :"))
# i = 1
# while i <= 10:
#     print(n,"X",i,"=",n*i)
#     i += 1

# reverse a string
# num = int(input("Enter number ="))
# reverse = 0
# while num > 0:
#     digit = num % 10
#     num = num // 10
#     reverse = reverse*10 + digit
# print("Reverse =",reverse)

# print even and odd digit in number
'''num = int(input("Enter number ="))
even_count = 0
odd_count = 0
while num > 0 :
    digit = num % 10
    if digit % 2 == 0:
       even_count += 1
    else:
       odd_count += 1
    num = num // 10
print("Even =",even_count)
print("Odd =",odd_count)'''

# # print sum of digits
# num = int(input("Enter a number ="))
# i = 1
# sum = 0
# while num > 0:
#     digit = num % 10  # get last digit
#     sum = sum + digit   
#     num = num // 10
# print("Sum of digits =",sum)

# print product of digits
# num = int(input("Enter number ="))
# product = 1
# while num > 0:
#     digit = num % 10    # get last digit
#     product = product*digit
#     num = num // 10
# print("Product of digits =",product)

# find largest digit
# num = int(input("Enter number :"))
# largest = 0
# while num > 0:
#     digit = num % 10
#     if digit > largest:
#       largest = digit
#     num = num //10
# print("Largest number =",largest)

# find smallest number
# num = int(input("Enter number :"))
# smallest = num % 10
# num = num // 10
# while num > 0:
#     digit = num % 10
#     if digit < smallest:
#         smallest = digit
#     num = num // 10
# print("Smallest number =",smallest)

# Check palindrome number
# num =int(input("Enter number ="))
# original = num
# reverse = 0
# while num > 0:
#     digit = num % 10
#     reverse = reverse*10 + digit
#     num = num // 10
# if original == reverse:
#     print("Palindrome")
# else:
#     print("Not palindrome")

# Factorial of a number
# num = int(input("Enter number ="))
# factorial = 1
# while num > 0 :
#     factorial = factorial*num
#     num = num - 1
# print("Factorial of number =",factorial)

# count zero digits in numbers
# num = int(input("Enter number ="))
# count_zero = 0
# while num > 0:
#     digit = num % 10
#     if digit == 0:
#         count_zero += 1
#     num = num // 10
# print("How many zeros present =",count_zero)

# find second largest digit
# num = int(input("Enter number ="))
# largest = 0
# second_largest = 0
# while num > 0:
#     digit = num % 10
#     if digit > largest :
#        second_largest = largest
#        largest  = digit
#     elif  digit > second_largest:
#         second_largest = digit
#     num = num // 10
# print("Largest is =",largest)
# print("Second largest is =",second_largest)

# num = input("Enter number =")
# total = 0
# for i in num:
#     total = total + int(i)
# print("Sum  =",total)

# for loop
# sum of odd digit in number
# num = input("Enter number =")
# total = 0
# for i in num:
#     if int(i) % 2 != 0:
#         total = total + int(i)
# print("Sum of odd number =",total)

# count even and odd digit in number
num = input("Enter number =")
even_count = 0
odd_count = 0
for i in num:
    if int(i) % 2 == 0:
        even_count += 1
    if int(i) % 2 != 0:
        odd_count += 1
    
print("Even digit =",even_count)
print("Odd digit =",odd_count)
    
    
    
    
    





    


    
    
    
