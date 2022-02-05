hours = float(input("enter hours; "))
rate = float(input("enter rate; "))
extra = (hours - 40)
pay = hours * rate
if hours <= 40:
    print(pay)
else:
    print("pay :", ((hours-extra) + (extra * 1.5)) * rate)

