def sq():
    s = int(input("Enter side of square: "))
    area = s * s
    print("Area of Square is:", area)

def rect(l, b):
    area = l * b
    print("Area of Rectangle is:", area)

def tri():
    b = int(input("Enter base: "))
    h = int(input("Enter height: "))
    area = 0.5 * b * h
    return area

def arc(radius):
    area = 3.14 * radius * radius
    print("Area of Circle is:", area)

print("---Menu---")
print("1.Square")
print("2.rectangle")
print("3.Triangle")
print("4.Circle")
ch=int(input("Enter ur Choice"))
if(ch==1):
    sq()
elif(ch==2):
    l=int(input("Enter Length:"))
    b=int(input("Enter Breadth:"))
    rect(l,b)
elif(ch==3):
    x=tri()
    print("Area of Triangle is :x")
elif(ch==4):
    radius=int(input("Enter the radius:"))
    y=arc(radius)
else:
    print("Invalid input")
    



    