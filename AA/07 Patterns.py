import turtle

window = turtle.Screen()
window.bgcolor("black")
window.title("Animation by Rhem")

t = turtle.Turtle()
t.fillcolor('green')
t.pensize(3)
t.speed(0)  # fastest 0, fast 10, normal 6, slow 3, slowest 1

t.up()
t.goto(0, -50)
t.down()
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.home()

t.goto(200, 200)
t.fillcolor('orange')
t.down()
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.home()

t.goto(-200, 200)
t.fillcolor('blue')
t.down()
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.home()


t.goto(-200, -200)
t.fillcolor('red')
t.down()
t.begin_fill()
t.circle(-50)
t.end_fill()

t.up()
t.home()

t.goto(200, -200)
t.fillcolor('yellow')
t.down()
t.begin_fill()
t.circle(-50)
t.end_fill()

t.up()
t.home()



turtle.exitonclick()