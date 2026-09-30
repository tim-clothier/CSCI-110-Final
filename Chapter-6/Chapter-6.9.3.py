days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
user_input = input("Enter a day by name: ").lower()

def day_num(day) :
    print(day)
    if (day in days) :
        return days.index(day)
    else :
        return "Invalid input."

print(day_num(user_input))