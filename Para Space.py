a = "Hi Sir,Myself mahalakshmi Coming from Trichy"
c = 0

for i in range(len(a)):
    if a[i] == " " and a[i+1]!=" ":
        c = c + 1

print("Number of words is:", c + 1)