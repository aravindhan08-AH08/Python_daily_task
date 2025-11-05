# 1. User Login System
# You’re building a simple login system.
#  User credentials are stored in a dictionary where the key is the username and the value is the password.
#  Write a function that:
# Takes username and password as input.
# Checks if the user exists and if the password matches.
# Prints:
# "Login Successful" if both match.
# "Invalid Password" if username exists but password is wrong.
# "User Not Found" if username doesn’t exist.
# Example Data:
# users = {
#     "alice": "pass123",
#     "bob": "qwerty",
#     "charlie": "hello123"
# }

def login_system(users, username, password):
    if username in users:
        if users[username] == password:
            print("Login Successful")
        else:
            print("Invalid Password")
    else:
        print("User Not Found")


users = {
    "alice": "pass123",
    "bob": "qwerty",
    "charlie": "hello123"
}

# Test cases
login_system(users, "alice", "pass123")     # Output: Login Successful
login_system(users, "bob", "wrongpass")     # Output: Invalid Password
login_system(users, "david", "anything")    # Output: User Not Found


# 2. Product Inventory Manager
# You have a product inventory stored as a dictionary:
#  Keys are product names, and values are their quantities.
# Write a program to:
# Add a new product or update quantity if it already exists.
# Print the updated inventory.
# Example:
# inventory = {"apple": 10, "banana": 5, "mango": 8}
# If input is "apple 4", total becomes 14.
#  If input is "grape 6", add it as a new product.