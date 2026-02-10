# Problem ena na oru number kudutha athu varaikkum even number thavira odd number * nu print pannanum.
# 2 code erukku oru code oru code list la print aagum innoru code list illama print aagum this is a different.
# a = int(input("Enter a Number: "))
# num = []

# for i in range(1, a + 1):
#     if i % 2 == 0:
#         num.append(i)
#     else:
#         num.append("*")

# print(num)

# intha code la [] use pannama print panna.
# list la print aagama normal ah print aagum intha code.
# a = int(input("Enter a Number: "))

# for i in range(1, a + 1):
#     if i % 2 == 0:
#         print(i, end=" ")
#     else:
#         print("*", end=" ")

# intha sum namma table panrathu example [3 x 1 = 3]

table = int(input("Enter table number: "))
end = int(input("Enter end limit: "))

for i in range(1, end + 1):
    print(table, "x", i, "=", table * i)
