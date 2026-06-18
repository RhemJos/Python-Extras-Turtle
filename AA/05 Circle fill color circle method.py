import turtle

window = turtle.Screen()
window.bgcolor("black")
window.title("Animation by Rhem")

t = turtle.Turtle()
t.color('green')
t.pensize(3)
t.speed(10)  # fastest 0, fast 10, normal 6, slow 3, slowest 1

t.circle(20)
t.pensize(3)
t.circle(-30)

t.color('red')
t.circle(100, extent=180)
t.reset()
t.speed(0)
t.color('blue')
t.pensize(3)
t.circle(100, extent=180,steps=7)
t.begin_fill()
t.fillcolor('yellow')
t.circle(75, steps=5)
t.end_fill()


turtle.exitonclick()