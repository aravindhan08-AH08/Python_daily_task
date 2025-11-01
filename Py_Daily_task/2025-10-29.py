# Class Assignment sir sonnaru max salary yaru vangunangalo avanga name print pannanum
name = ["Alice", "John", "Farhana", "Ruben"]
salary = [50000, 20000, 50000, 25000]
max = salary[0]

for i in range (len(salary)):
    if salary[i] > max:
        max = salary[i]
for i in range (len(salary)):
    if salary[i] == max:
        print(name[i])



# Question 1
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient balance! {self.name} has only {self.balance}.")
        else:
            self.balance -= amount
            print(f"{self.name} withdrew {amount}. New balance: {self.balance}")

    def show_balance(self):
        print(f"Account Holder: {self.name} | Balance: {self.balance}")


# Create two accounts
acc1 = BankAccount("Aravindhan", 1000)
acc2 = BankAccount("Kumar", 500)

# Show initial balances
acc1.show_balance()
acc2.show_balance()

# Deposit money
acc1.deposit(500)
acc2.deposit(200)

# Withdraw money
acc1.withdraw(300)
acc2.withdraw(800)  # insufficient balance warning

# Final balances
acc1.show_balance()
acc2.show_balance()


# Question 2
class LibraryBook:
    def __init__(self, title, author, available_copies):
        self.title = title
        self.author = author
        self.available_copies = available_copies

    def borrow_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print(f"Book borrowed: {self.title}")
            print(f"Available copies: {self.available_copies}")
        else:
            print("Book not available!")

    def return_book(self):
        self.available_copies += 1
        print(f"Book returned: {self.title}")
        print(f"Available copies: {self.available_copies}")

    def show_status(self):
        print(f"Title: {self.title} | Author: {self.author} | Available copies: {self.available_copies}")



book1 = LibraryBook("Harry Potter", "J.K. Rowling", 2)
book2 = LibraryBook("Rich Dad Poor Dad", "Robert Kiyosaki", 1)


book1.show_status()
book2.show_status()


book1.borrow_book()
book1.borrow_book()
book1.borrow_book()  


book1.return_book()


book1.show_status()
book2.show_status()
