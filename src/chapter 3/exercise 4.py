Name = input("Enter your name:")
try:
    age = int(input("enter age"))
    if age >= 18:
        print("Dear,",Name,"you can vote")
    elif 0 <= age <=17:
        print("Dear",Name," too young to vote")
    else:
        print("Dear,",Name," you are a time traveller")
except:
    print("enter integer")