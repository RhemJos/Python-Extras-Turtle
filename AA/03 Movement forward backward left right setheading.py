import turtle

t = turtle.Turtle()
t.setheading(90)  # 90, 180, 270, 360
t.color("blue", "green")
t.pensize(10)
t.forward(100)
t.pensize(30)
t.fd(50)

window = turtle.Screen()
window.bgcolor("black")
window.title("Animation by Rhem")
turtle.exitonclick()


