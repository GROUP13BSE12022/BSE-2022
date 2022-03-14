while True:
    file_name = input("enter file name :")
    if file_name.lower() == "na na boo boo":
        print("NA NA BOO BOO TO YOU - YOU have been punk'd!")
        break
    try:
        file = open(file_name,"r")
    except:
        print("file cant be opened :",file_name)
        continue
    total = 0
    count = 0
    for line in file:
        if line.startswith("X-DSPAM-Confidence:"):
            line = line.strip("\n") and float(line.strip("X-DSPAM-Confidence"))
            total += line
            count += 1
    print("Average spam confidence: ",total/count)
    print('please try entering me "na na boo boo"')