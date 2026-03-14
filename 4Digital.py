input1 = int(input("Enter first 4-digit number: "))
input2 = int(input("Enter second 4-digit number: "))
input3 = int(input("Enter third 4-digit number: "))


d1 = [int(d) for d in str(input1)]
d2 = [int(d) for d in str(input2)]
d3 = [int(d) for d in str(input3)]

largest_sum = max(d1) + max(d2) + max(d3)
smallest_sum = min(d1) + min(d2) + min(d3)
key = largest_sum *smallest_sum

print("Key =", key)
