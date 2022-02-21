total = 0
count = 0
average = 0
while True:
    data = input("enter number :")
    try:
        number = float(data)
        total = total + number
        count = count + 1
        average = total / count
    except:
        if data == "done":
            break
        else:
            print("invalid data")
print("total:",total,"count:",count,"average:",average)

