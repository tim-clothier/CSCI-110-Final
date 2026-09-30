# Problem 1:    Take the sentence: All work and no play makes Jack a dull boy. Store each word in a separate variable, then print out the sentence on one line using print.

ALL = "All"
work = "work"
AND = "and"
no = "no"
play = "play"
makes = "makes"
jack = "Jack"
a = "a"
dull = "dull"
boy = "boy"

print (ALL + ' ' + work + ' ' + AND + ' ' + no + ' ' + play + ' ' + makes + ' ' + jack + ' ' + a + ' ' + dull + ' ' + boy + '.')

# Problem 2:    Add parenthesis to the expression 6 * 1 - 2 to change its value from 4 to -6.

print (6 * 1 - 2)
print (6 * (1 - 2))

# Problem 3: Place a comment before a line of code that previously worked, and record what happens when you rerun the program.

print ("This is functional text")
# print ("This is not functional text")

# Problem 4: Start the Python interpreter and enter bruce + 4 at the prompt. This will give you an error:

#    NameError: name 'bruce' is not defined

#Assign a value to bruce so that bruce + 4 evaluates to 10.

# print (bruce + 4)
# This line doesn't work - bruce is treated as an unassigned variable.

bruce = 6
print (bruce + 4)

# Problem 5: The formula for computing the final amount if one is earning compound interest is given on Wikipedia as

# A = P * (1 + r / n) ^ (n * t)

# Write a Python program that assigns the principal amount of $10000 to variable P, assign to n the value 12, and 
# assign to r the interest rate of 8%. Then have the program prompt the user for the number of years t that the money will be compounded for.
# Calculate and print the final amount after t years.

P = 10000
n = 12
r = 0.08
t = int(input("Enter the number of years the money will be compounded for: "))

A = P * (1 + r / n) ** (n * t)

print ("Total amount after " + str(t) + " years:" + str(A))

# Problem 6: Evaluate the following numerical expressions in your head, then use the Python interpretor to check your results
#>>> 5 % 2 = 1
#>>> 9 % 5 = 4
#>>> 15 % 12 = 3
#>>> 12 % 15 = 12
#>>> 6 % 6 = 0
#>>> 0 % 7 = 0
#>>> 7 % 0 = Fails to run

print (5 % 2)
print (9 % 5)
print (15 % 12)
print (12 % 15)
print (6 % 6)
print (0 % 7)
#print (7 % 0)

#Problem 7: You look at the clock and it is exactly 2pm. You set an alarm to go off in 51 hours. At what time does the alarm go off?
# (Hint: you could count on your fingers, but this is not what we’re after. If you are tempted to count on your fingers, change the 51 to 5100.)
# 51 hours - multiple of 24 (48) leaves 3 hours remaining. 2pm + 3 hours = 5pm. The alarm goes off at 5pm.

#Problem 8: Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours), 
# and ask for the number of hours to wait. Your program should output what the time will be on the clock when the alarm goes off.

currentTime = int(input("Enter the current time in hours (0-23): "))
waitTime = int(input("Enter the number of hours to wait: "))

print("The alarm will go off at " + str((currentTime + waitTime) % 24))