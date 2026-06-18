import turtle

window = turtle.Screen()
window.bgcolor("black")
window.title("Animation by Rhem")

t = turtle.Turtle()
t.pensize(10)
t.speed(0)  # fastest 0, fast 10, normal 6, slow 3, slowest 1
t.hideturtle()
t.color('green')

t.begin_fill()
t.fillcolor('light blue')
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)

t.end_fill()

turtle.exitonclick()