while True:
    file_name = input("enter file name :")
    try:
        file = open(file_name,"r")
        break
    except:
        print("file cant be opened :",file_name)
total = 0
count = 0
for line in file:
    if line.startswith("X-DSPAM-Confidence:"):
        line = line.strip("\n") and float(line.strip("X-DSPAM-Confidence"))
        total += line
        count += 1
print("Average spam confidence: ",total/count)