# Level 2
# question 5
color = input("Enter Traffic Light Color: ").upper()

if color == "RED":
    print("Stop")
elif color == "YELLOW":
    print("Ready")
elif color == "GREEN":
    print("Go")
else:
    print("Invalid Input")

# Question 6
hour = int(input("How many Hour: "))

if hour < 0:
    print("Invalid Input")
elif hour <= 2:
    print(0)
elif hour <= 5:
    print(hour * 20)
elif hour <= 10:
    print(hour * 15)
else:
    print("Invalid Input")