while True:
    try:
        file_name = input("enter the file :")
        file = (file_name,"r")
        break
    except:
        print("file cant be opened")
count = 0
for line in file:
    if line.startswith("from"):
        line1 = line.strip("\n") and line.strip()
        count +=1
        print(line1[1])
print("count :",count)