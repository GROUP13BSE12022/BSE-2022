try:
    people = int(input("enter number of people:"))
    if 0 <= people <= 50:
        print("$4000")
    elif 50 <= people <= 100:
        print("$10000")
    elif 100 <= people <= 200:
        print("$15000")
    elif people > 200:
        print("$20000")
    else:
        print("error")
except:
    print("error... Enter an integer")