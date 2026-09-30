days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

user_input = int(input("Enter an integer, 0-6"))

def day_name(num) :
    if (num <= 6 and num >= 0) :
        return days[num]
    else :
        print ("Invalid input.")
        return
    
print(day_name(user_input))