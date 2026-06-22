import turtle

window = turtle.Screen()
window.bgcolor("black")
window.title("Animation by Rhem")

t = turtle.Turtle()
t.color('green')
t.pensize(3)
t.speed(10)  # fastest 0, fast 10, normal 6, slow 3, slowest 1

t.circle(100)
t.undo()

t.reset()
t.speed(0)
# t.penup()
t.up()
t.goto(0,-100)
t.down()
t.circle(100)

p = turtle.Pen()
p.color('red')
p.circle(50)

'''
Turtle is the same as Pen
'''



turtle.exitonclick()