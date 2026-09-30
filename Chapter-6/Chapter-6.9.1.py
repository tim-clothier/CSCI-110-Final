directions = ["N", "E", "S", "W"]

user_input = input("Enter a cardinal direction: N, E, S, or W.").upper()

def turn_clockwise (direction) :
    if direction in directions:
        idx = directions.index(direction)
        if idx == 3 :
            return directions[0]
        else :
            idx += 1
            return directions[idx]
    else :
        print ("Incorrect input - should be N, E, S, or W")

print(turn_clockwise(user_input))