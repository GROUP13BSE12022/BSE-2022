try:
    location = input("Enter location:")
    pay = int(input("Enter amount:"))
    if location == "Mbarara":
        if pay > 4000000:
            print("Sure, I can work with this")
        else:
            print("No thanks, I can find something better")
    elif location == "space":
        if pay >= 0:
            print("without doubt i will take it")
        else:
            print("without doubt i will take it")
    elif location == "kampala":
        if pay >= 10000000:
            print("sure i can work")
        else:
            print("no way!")
    else:
        if pay >= 6000000:
            print("sure i can work")
        else:
            print("no way")
except:
    print("error")

