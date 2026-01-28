# # Level 2
# Question 3
amount = int(input("Enter ur total bill amount: "))

if amount >= 1000:
    discount = amount * 0.10
elif amount >= 500:
    discount = amount * 0.05
else:
    discount = 0

final_price = amount - discount

print("Discount: ", int(discount))
print("final_price: ", int(final_price))

# Question 4
# Ithula amount varathu so Profit or Loss nu mattum tha varum
cost_price = int(input("Enter ur cost:"))
selling_price = int(input("Enter ur selling price: "))

if selling_price > cost_price:
    print("PROFIT")
elif selling_price < cost_price:
    print("LOSS")
else:
    print("NO PROFIT NO LOSS")

# Intha code la run panna Amount oda yellam senthu varum
cost_price = int(input())
selling_price = int(input())

if selling_price > cost_price:
    print("PROFIT")
    print("Amount:", selling_price - cost_price)
elif selling_price < cost_price:
    print("LOSS")
    print("Amount:", cost_price - selling_price)
else:
    print("NO PROFIT NO LOSS")
