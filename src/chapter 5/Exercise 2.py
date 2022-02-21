total_number = 0
number_of_times = 0
list_of_numbers_entered = []
while True:
    data = input("enter number :")
    try:
        number = float(data)
        total_number += number
        number_of_times += 1
        list_of_numbers_entered.append(number)
    except:
        if data == "done":
            break
        else:
            print("wrong data")
print("Largest", max(list_of_numbers_entered), "Smallest", min(list_of_numbers_entered))
