#(a) Declare the following variables and print their data types using type():
name = "Rakibul Islam Bhuiyan"
age = 23
cgpa = 3.75
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

# type conversions and print the results:
# String to integer
num_str = "12345"
num_int = int(num_str)
print(num_int)

# Integer to string
num = 530
num_str2 = str(num)
print(num_str2)

# Float to integer
float_num = 3.75
int_num = int(float_num)
print(int_num)
# Explanation: The decimal part is truncated (not rounded)

# Integers to boolean
print(bool(1))  # True
print(bool(0))  # False

"""**Question 2: Operators**"""

a = 20
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

print("Floor Division:", a // b)
print("Modulus:", a % b)

print("Power:", a ** b)

#Comparison results
print("20 > 5:", a > b)
print("20 == 5:", a == b)
print("20 != 5:", a != b)

"""**Question 3: String Manipulation**"""

name = "python programming"

print(name.upper())
print(name.title())
print(name.replace("programming", "language"))
print(len(name))

name = "Rakibul Islam Bhuiyan"
age = 23
cgpa = 3.53

#Using an f-string
print(f"My name is {name}, I am {age} years old, and my GPA is {cgpa}")

"""**Question 4: Conditional Statements  Intermediate**"""

# Age Checker
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age > 18:
    print("You are an adult")
elif 13 <= age <= 17:
    print("You are a teenager")
else:
    print("You are a child")

#Even / Odd using a ternary operator in a single line:
num = int(input("Enter a number: "))
print("This is an even number" if num % 2 == 0  else "This is an odd number")

#Grade Calculator
mark=int(input("Enter your mark:"))

if mark < 0 or mark > 100:
  result="Invalid mark"
elif mark >= 90 and mark <= 100:
  result="A+"
elif mark >= 80 and mark <= 89:
  result="A"
elif mark >= 70 and mark <= 79:
  result="B"
elif mark >= 60 and mark <= 69:
  result="C"
elif mark >= 50 and mark <= 59:
  result="D"
else:
  result="Fail"

print(f"Your grade is {result}")

# Login System
correct_username = "Admin"
correct_password = "12345"

attempts = 0
max_attempts = 3 #counter

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print(f"Login successful! Welcome, {username}.")
        break
    elif username == correct_username and password != correct_password:
        print("Incorrect password. Try again.")
    else:
        print("User not found.")

    attempts = attempts+1

if attempts == max_attempts:
    print("Account locked.")

"""**Question 5: ATM Simulation — Extend the Program**"""

#an ATM program with the following variables: pinNumber, balance, and request:
pinNumber = 2026
balance = 5000

pin = int(input("Enter your PIN: "))

if pin == pinNumber:
    request = int(input("Enter withdrawal amount: "))

    if request > 500 and request <= balance:
        balance = balance - request
        print("Withdrawal successful.")
        print(f"Remaining balance:{balance}")
    elif request > balance:
        print("Insufficient balance.")
    else:
        print("Withdrawal amount must be greater than 500.")
else:
    print("Wrong PIN.")

#an attempts counter
pinNumber = 2026
balance = 5000
attempts = 3 #counter

while attempts > 0:
    pin = int(input("Enter your PIN: "))

    if pin == pinNumber:
        request = int(input("Enter withdrawal amount: "))

        if request > 500 and request <= balance:
            balance = balance - request
            print("Withdrawal successful.")
            print(f"Remaining balance: {balance}")
        elif request > balance:
            print("Insufficient balance.")
        else:
            print("Withdrawal amount must be greater than 500.")
        break
    else:
        attempts = attempts - 1
        print(f"Wrong pin. Attempts remaining: {attempts}")

        if attempts == 0:
            print("Card blocked.")

#Login System before the ATM:
correct_username = "Admin"
correct_password = "12345"

is_active = True #flag

username = input("Enter username: ")
password = input("Enter password: ")

if username=="Admin" and password=="12345" and is_active:
  print("Login successful. Proceed to ATM pin check...")
else:
  print("Account is disabled.")

"""**Question 6: Basic Loops** ,**For Loop**"""

#Print numbers from 1 to 20
for x in range(1,21):
    print(x)

#Multiplication table of 7
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

#Sum of numbers from 1 to 100
total = 0
for i in range(1, 101):
    total = total + i
print(f"Sum of numbers from 1 to 100: {total}")

#Even numbers between 1 and 50
for i in range(2, 51, 2):
    print(i)

#Fruits list with position
fruits = ['apple', 'banana', 'cherry', 'mango', 'grape']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

"""**While loop**"""

#Print numbers from 10 down to 1
i = 10
while i >= 1:
    print(i)
    i = i - 1

#Sum of positive numbers until 0 or negative is entered
total = 0
while True:
    num = int(input("Enter a number: "))
    if num <= 0:
        break
    total = total + num
print(f"The total sum of all numbers: {total}")

#Countdown with Blast off
count = 10
while count >= 0:
    if count == 0:
        print("Blast off!")
    else:
        print(count)
    count = count - 1

#First 10 multiples of 6
i = 1
while i <= 10:
    print(6 * i)
    i = i + 1