days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]



def print_day():
    day = input("Enter the number corresponding to a weekday (0-6)")
    print(str(days[int(day)]))

print_day();