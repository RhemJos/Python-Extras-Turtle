import turtle

tortuga = turtle.Turtle()

tortuga.shape("turtle")

# This will show the line color and the color for the turtle:
# tortuga.color()

tortuga.forward(100)

tortuga.color("red")  # it will change both colors
tortuga.forward(100)
tortuga.color("blue", "green")
tortuga.backward(300)

# to set the color mode to RGB:
# turtle.colormode(255)
# tortuga.color(120,40,50)
