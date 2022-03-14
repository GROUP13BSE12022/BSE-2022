while True:
    try:
        file_name = input("enter file name :")
        file = open(file, "r")
        break
    except:
        print("file cant be open :",file_name)
for line in file:
    print(line.upper())