try:
    measles = open("measles.txt", "r")
    file_nam = input("enter file name:")
    new_file = open(file_nam, "w")
    year = input("enter year: ").lower()
    if 0 <= len(year) <= 4:
        try:
            if year == "" or year == 'all' or int(year):
                for line in measles:
                    if ((year == "")or(year ==line[88:89])or(year ==line[88:90])or(year==line[88:91])or(year==line[88:92])or(year=="all")):
                        new_file.write(line)
        except:
            exit("invalid year")
    else:
      print("incorrect year input")
except:
    exit("file not found")

