"""**Question 1**"""
class Car:
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self, amount):
        self.speed = self.speed + amount
        print(f"Accelerated by {amount}. Current speed: {self.speed}")

    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0
        print(f"Braked by {amount}. Current speed: {self.speed}")

    def display_info(self):
        print("Car Details:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Current Speed: {self.speed}")
        print("-" * 30)

#Create 2 car objects
car1 = Car("BMW", "Coupé", 2020)
car2 = Car("Bantley", "Flagship", 2022)

#Call car1
car1.display_info()
car1.accelerate(40)
car1.brake(10)
car1.display_info()

#Call car2
car2.display_info()
car2.accelerate(60)
car2.brake(70)
car2.display_info()

"""**Question 2**"""

class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        self.transactions = []   # to store transaction history

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transactions.append(f"Deposited: {amount}")
        print(f"Welcome {self.account_holder}!")
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient balance!")
        else:
            self.balance = self.balance - amount
            self.transactions.append(f"Withdrawn: {amount}")
            print(f"Withdrawn {amount}. New balance: {self.balance}")

    def get_balance(self):
        print(f"Current Balance: {self.balance}")

    def transaction_history(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)
        print("-" * 30)


#2 bank account objects
account1 = BankAccount("Rakib", "ACC1001")
account2 = BankAccount("Maruf", "ACC1002")

#Perform transactions on account1
account1.deposit(1000)
account1.withdraw(300)
account1.deposit(500)
account1.get_balance()
account1.transaction_history()

#Perform transactions on account2
account2.deposit(2000)
account2.withdraw(700)
account2.withdraw(1500)  # insufficient balance case
account2.get_balance()
account2.transaction_history()

"""**Question-3**"""

class Book:
    def __init__(self, title, author, isbn, is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to library.")

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.is_available:
                book.is_available = False
                print(f"You borrowed '{book.title}'.")
                return
        print("Book not available or ISBN not found.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.is_available:
                book.is_available = True
                print(f"You returned '{book.title}'.")
                return
        print("Invalid return attempt.")

    def show_available_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            if book.is_available:
                print(f"{book.title} by {book.author}")
        print("-" * 30)


# Create Library
library = Library("City Library")

# Add at least 4 books
book1 = Book("Python Basics", "John Smith", "ISBN001")
book2 = Book("Data Science", "Jane Doe", "ISBN002")
book3 = Book("Machine Learning", "Andrew Ng", "ISBN003")
book4 = Book("AI Fundamentals", "Alan Turing", "ISBN004")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

#Borrow 2 books
library.borrow_book("ISBN001")
library.borrow_book("ISBN003")

#Return 1 book
library.return_book("ISBN001")

#Show available books
library.show_available_books()

"""**Question -4**"""

class Employee:
    total_employees = 0

    def __init__(self, name, employee_id, department, salary):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary
        Employee.total_employees = Employee.total_employees + 1

    def give_raise(self, percent):
        self.salary += self.salary * percent / 100

    def details(self):
        print(self.name, self.employee_id, self.department, self.salary)


# Creating employees
e1 = Employee("Sajjad", 101, "HR", 50000)
e2 = Employee("Imran", 102, "IT", 60000)
e3 = Employee("Rakib", 103, "Assistent Sceritary", 45000)

e1.give_raise(10)
e2.give_raise(15)

e1.details()
e2.details()
e3.details()

print("Total employees:", Employee.total_employees)

"""**Question -5**"""

class ShoppingCart:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, name, price, quantity):
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def remove_item(self, name):
        self.items = [item for item in self.items if item["name"] != name]

    def total_price(self):
        return sum(item["price"] * item["quantity"] for item in self.items)

    def show_cart(self):
        print(f"Cart for {self.customer_name}:")
        for item in self.items:
            print(item)
        print("Total:", self.total_price())


# Shopping carts
cart1 = ShoppingCart("Sajjad")
cart2 = ShoppingCart("Imran")

cart1.add_item("Apple", 2, 5)
cart1.add_item("Milk", 3, 2)
cart1.add_item("Bread", 2, 1)
cart1.remove_item("Milk")
cart1.show_cart()

cart2.add_item("Rice", 10, 1)
cart2.add_item("Oil", 8, 2)
cart2.add_item("Sugar", 4, 3)
cart2.remove_item("Oil")
cart2.show_cart()