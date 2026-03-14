name = ['Tom','Jerry','Abi','Amu','Geetha']
marks = [[30,40,50],[67,88,90],[90,76,72],[90,76,67],[60,70,45]]

for i in range(len(name)):
    total = sum(marks[i])
    per = int(total / len(marks[i]))   

    if per <= 40:
        grade = "F Grade"
    elif per <= 60:
        grade = "B Grade"
    elif per <= 90:
        grade = "A Grade"
    else:
        grade = "S Grade"

    print(name[i], "-", per, "%", "-", grade)