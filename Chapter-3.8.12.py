import turtle
wn = turtle.Screen()
joey = turtle.Turtle()
joey.color("black")
joey.speed(1)
joey.shape("turtle")
wn.bgcolor = "lightblue"

#Set center stamp
joey.stamp()
joey.penup()

for i in range(12):
    joey.forward(100)
    joey.stamp()
    joey.forward(-100)
    joey.right(30)

turtle.exitonclick()