# Create user account
import csv
user = input("Enter user name :")
email = input("Enter user Email :")
password = input("Enter password :")
confirm_pass = input("Enter confirm password :")
if password == confirm_pass:
    with open("UserRegistration.csv","a",newline="") as f:
        writer = csv.writer(f)
        writer.writerow([user , email, password])
    print("Account created successfully")
else:
    print("Password does not match")

# saved data check during login
import csv
user = input("Enter user name :")
password = input("Enter password :")
found = False
with open("UserRegistration.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        if (row[1]) == email and (row[2]) == password:
            found = True
            break
if found:
    print("Login successfully")
else:
    print("Invalid email or password")

