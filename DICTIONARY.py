s = input("Enter the string: ")

d = {'A':1, 'B':10, 'C':100, 'D':1000}

total = 0

for i in s:
    total = total + d[i]

print("Sum =", total)