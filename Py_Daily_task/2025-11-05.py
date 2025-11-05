def login_system(users, username, password):
    if username in users:
        if users[username] == password:
            print("Login Successful")
        else:
            print("Invalid Password")
    else:
        print("User Not Found")


# Example data
users = {
    "alice": "pass123",
    "bob": "qwerty",
    "charlie": "hello123"
}

# Test cases
login_system(users, "alice", "pass123")     # Output: Login Successful
login_system(users, "bob", "wrongpass")     # Output: Invalid Password
login_system(users, "david", "anything")    # Output: User Not Found