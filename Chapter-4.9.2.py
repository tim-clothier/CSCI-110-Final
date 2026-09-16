import turtle

def draw_square(size, startx, starty):
    turt = turtle.Turtle()
    turt.speed = 1
    turt.hideturtle()
    turt.penup()
    turt.setpos(startx, starty)
    turt.pendown()
    for i in range(4):
        turt.forward(size)
        turt.right(90)
    #turt.pendown()

for i in range(5):
    x = 0
    y = 0
    j = i + 1
    draw_square(20 + (j * 20), x - j * 10, y + j * 10)