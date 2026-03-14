def prime_factor(n):
    i = 2
    while i <= n:
        if n % i == 0:
            print(i, end=" ")
            n = n // i
        else:
            i = i + 1

num = int(input("Enter any number: "))
prime_factor(num)