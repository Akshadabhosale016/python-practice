# read data from file
'''f = open ("Practice.txt","r")
data = f.read()
print(data)
f.close()

# read first line in data
f = open("Practice.txt","r")
print(f.readline())
f.close()

# read every line in data
f = open("Practice.txt","r")
data = f.readlines()
print(data)
f.close()

f = open ("Practice.txt","r")
for line in f:
    print(line)

# Write data in file
f = open("Practice.txt","w")
f.write("Python\nIntermediate\nFile Handling")
f.close()

# Append data in file
f = open("Practice.txt","a")
f.write("\nI love python")
f.close()

# create a new file
f = open("Student.txt","x")
f.close()

# delete a file
import os
os.remove("Student.txt")

# read data from file and count number of lines
f = open("Practice.txt","r")
count = 0
for line in f:
    count += 1
print("Total number of lines =",count)
f.close()

# read data from file and count number of words
f = open("Practice.txt","r")
data = f.read()
count = data.count("Python")
print("Python count =",count)
f.close()

# using with() write data in file
with open("Practice.txt","w") as f:
    f.write("Python\nFile Handling\nDay 2")

# using with() append data in file
with open("Practice.txt","a") as f:
    f.write("\nI am learning python\nFile handling is easy")

# using with() count lines in file
with open("Practice.txt","r") as f:
    count = 0
    for line in f:
        count += 1
print("Lines in file =",count)

# using with() count given word in file
with open("Practice.txt","r") as f:
    data = f.read()
    count = data.lower().count("python")
    print("Python count =",count)

with open("Practice.txt","r") as f:
    data = f.read()
    if "Python" in data:
        print("Python is present")
    else:
        print("Not present")

# copy data from one file to another file
with open("Practice.txt","r") as f:
    data = f.read()
with open("Backup.txt","w") as f:
    f.write(data)'''
# delete a file
'''import os
os.remove("Backup.txt")

# count words and lines in file
with open("Practice.txt","r") as f:
    data = f.read()
total_lines = len(data.splitlines())
total_words = len(data.split())
print("Total lines =",total_lines)
print("Total words =",total_words)

# count given word in file and print line number
with open("Practice.txt","r") as f:
    data = f.readlines()
for line in data:
    if "Python" in line:
        print(line,end ="")

# count given word in file and print line number
with open("Practice.txt","r") as f:
    data = f.readlines()
count = 0
for line in data:
    if "Python" in line:
        count += 1
        print(f"{count}.{line}",end ="")


with open("Practice.txt","r") as f:   # copy one file in another file
    data = f.readlines()
with open("Python.txt","w") as f:
   for line in data:
     if "Python" in line:
       f.write(line)
#import os
#os.remove("Python.txt")

# count given win file
with open("Practice.txt","r") as f:
    data = f.readlines()
count = 0
for line in data:
    if line.strip() == "Python" :
      count += 1
print("Python count =",count)

# count given word in file
with open("Practice.txt","r") as f:
    data = f.readlines()
python_count= 0
java_count = 0
C_count = 0
for line in data:
    if "Python" in line:
        python_count += 1
    if "Java" in line:
        java_count += 1
    if "C++" in line:
        C_count += 1
print("Python =", python_count)
print("Java =",java_count)
print("C++ =",C_count)

# count total character in file
with open("Practice.txt","r") as f:
    data = f.read()
total_character = len(data.replace("\n",""))
print("Total character =",total_character)

# count total character in given d in file
with open("Practice.txt","r") as f:
    data = f.readlines()
total_character = 0
for line in data:
    if line.strip() == "Python":
        total_character += len(line.strip())
print("Total character = ",total_character)'''







   



