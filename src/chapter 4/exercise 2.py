c = float(input("enter initial amount:"))
r = float(input("enter yearly rate:"))
n = float(input("enter interest per year:"))
t = float(input("enter years till maturation:"))
p = c*((1+ r/n)**(t*n))
print(p)