# # List
# fruits = ["apple", "banana", "mango", "orange"]
# print(fruits[0])   # first element
# print(fruits[2])   # third element
# print(fruits[-1])   # last element

# numbers = [10, 20, 30, 40, 50]
# print(numbers[0])  # first element
# print(numbers[-1])  # last element
# print(numbers[2])   # element at index 2

# students = ["Yash", "Akshada", "Rahul", "Sneha"]
# print(students[-1])  # last element
# print(students[-2])   # second last element

# # list slicing
# fruits = ["apple", "banana", "mango", "orange", "grapes"]
# print(fruits[0:3])      # first 3 element
# print(fruits[2:])       # from index 2 to end
# print(fruits[: : 2])    # even index

# students = ["Yash", "Akshada", "Rahul", "Sneha", "Om"]
# print(students[::-1])   # reverse

# numbers = [10, 20, 30, 40, 50, 60, 70, 80]
# print(numbers[4:])  # last 4 element

# numbers = [10, 20, 30, 40, 50, 60]
# print(numbers[1:5])

# # list updating
# fruits = ["apple", "banana", "mango"]
# fruits[1] = "orange"
# print(fruits)

# marks = [80, 75, 90, 65, 70]
# marks[3] = 85
# print(marks)

# students = ["Yash", "Akshada", "Rahul", "Sneha"]
# students[-1] = "Om"
# print(students)

# numbers = [10, 20, 30, 40, 50]
# numbers[1:3] = [200,300]
# print(numbers)

# colors = ["red", "green", "blue", "yellow"]
# colors[1:3] = "Pink","Black"
# print(colors)

# # adding element to a list
# fruits = ["apple", "banana", "mango"]
# fruits.append("Orange")   # element add to end
# print(fruits)

# numbers = [10, 20, 30, 40]
# numbers.insert(2,25) # element add at index 2
# print(numbers)

# students = ["Yash", "Akshada"]
# students.extend(["Rahul","Sneha"])
# print(students)

# colors = ["red", "blue"]
# colors.append("Green")
# colors.extend(["Yellow","Pink"])
# print(colors)

# # remove element from list
# fruits = ["apple", "banana", "mango", "orange"]
# fruits.remove("banana")     # remove by value
# print(fruits)   

# numbers = [10, 20, 30, 40, 50]
# numbers.pop(2)   # remove by index
# print(numbers)

# students = ["Yash", "Akshada", "Rahul"]
# students.pop()  # removed without index
# print(students)

# colors = ["red", "green", "blue"]
# colors.clear()   # remove list
# print(colors)

# # List methods
# numbers = [10, 20, 30, 40, 50]
# print(len(numbers))   # length of list

# numbers = [50, 20, 40, 10, 30]
# numbers.sort()    # sort the list in asecending order
# print(numbers)
# numbers.sort(reverse=True)   # sort the list in descending  order
# print(numbers)

# numbers = [10, 20, 30, 40, 50]
# numbers.reverse()  # reverse the list
# print(numbers)

# numbers = [10, 20, 10, 30, 10, 40]
# print(numbers.count(10))   # count the number of 10 in list

# students = ["Yash", "Akshada", "Rahul", "Sneha"]
# print(students.index("Rahul"))  # index of rahul in list

# # List with loops
# fruits = ["apple", "banana", "mango", "orange"]
# for fruit in fruits:
#     print(fruit)

# # print odd numbers
# numbers = [10, 15, 20, 25, 30, 35]
# for num in numbers:
#   if num % 2 != 0:
#      print(num)

# # calculate sum
# numbers = [10, 20, 30, 40, 50]
# total = 0
# for num in numbers:
#    total = total + num
# print(total)

# # smallest number
# numbers = [25, 10, 45, 30, 15]
# smallest = numbers[0]
# for num in numbers:
#    if num < smallest:
#       smallest = num
# print("Smallest =",smallest)

# # count even and odd
# numbers = [10, 25, 30, 45, 50, 65]
# even_num = 0
# odd_num = 0
# for num in numbers:
#    if num % 2 == 0:
#       even_num += 1
#    else:
#       odd_num += 1
# print("Even number =",even_num)
# print("Odd number =",odd_num)

# # Largest number
# numbers = [25, 10, 45, 30, 15]
# largest = numbers[0]
# smallest = numbers[0]
# for num in numbers:
#    if num > largest:
#       largest = num
#    if  num < smallest:
#       smallest = num
# print("Largest =",largest)
# print("Smallest =",smallest)

# # Average of list
# numbers = [10, 20, 30, 40, 50]
# total = 0
# for num in numbers:
#    total = total + num
# average = total / len(numbers)
# print("Average",average)

# # found 30 in list
# numbers = [10, 20, 30, 40, 50]
# if 30 in numbers:
#     print("30 found")
# else:
#     print("NOT found")

# # find 20 number at index
# numbers = [10, 20, 30, 20, 40, 20, 50]
# print("20 occur =",numbers.count(20))

# # Print list in reverse
# numbers = [10, 20, 30, 40, 50]
# for i in range(len(numbers)-1, -1, -1):
#    print(numbers[i])
















      


 




