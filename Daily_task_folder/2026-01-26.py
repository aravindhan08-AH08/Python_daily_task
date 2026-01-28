# Level 2
# Question 1
n=int(input("Enter one number: "))

days = ["Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday", "Sunday"]

if 1 <= n <= 7:
    print(days[n-1])
else:
    print("Invalid Input")

# Question 2
a = int(input("Enter one number: "))
b = int(input("Enter one number: "))
c = int(input("Enter one number: "))

if a == b == c:
    print("All are the numbers equal: ", a)
elif a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)