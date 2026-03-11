a = input("Enter your password: ")

up = 0
sm = 0
dg = 0
sp = 0

if(len(a) > 7):
    for i in a:
        if(i.isupper()):
            up = up + 1
        elif(i.islower()):
            sm = sm + 1
        elif(i.isdigit()):
            dg = dg + 1
        else:
            sp = sp + 1

    if up > 0 and sm > 0 and dg > 0 and sp > 0:
        print("Password is strong")
    else:
        print("Password is weak")
else:
    print("Weak password, please satisfy the condition")