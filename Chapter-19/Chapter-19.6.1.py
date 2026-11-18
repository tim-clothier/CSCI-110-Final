# Write a function named readposint that uses the input dialog to prompt the user for a positive integer and then checks the input to confirm that it meets the requirements.
# It should be able to handle inputs that cannot be converted to int, as well as negative ints, and edge cases (e.g. when the user closes the dialog, or does not enter anything at all.)

def getuserinput() :
    user_input = input("Enter a positive integer: ")
    print("User input: " + user_input)
    return user_input

def isint(val) :
    try:
        value = int(val)
    except:
        raise ValueError("Input value \"{0}\" is a {1}, and couldn't be converted to integer".format(val, type(val)))

def hasvalue(val) :
    if val == "" :
        raise ValueError("No input detected")
    else :
        return True

def ispos(val) :
    if val <= 0 :
        error = "Input was a non-positive integer"
        raise ValueError("{0} is a non-positive integer".format(val))
    else :
        return True

def readposint() :
    val = getuserinput()
    hasvalue(val)
    isint(val)

    intval = int(val)

    ispos(intval)

    print("Success! {0} is a verified positive integer".format(val))

readposint()

