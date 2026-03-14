name = ['Tom','Jerry','Abi','Amu','Geetha']
age = [20,18,19,25,23]
location = ['CHENNAI','TRICHY','PONDY','TRICHY','CHENNAI']

res = list(zip(age, name, location))
res2 = sorted(res)

for i in range(5):
    print("{}. {} age is {} lives in {}".format(i+1, res2[i][1], res2[i][0], res2[i][2]))