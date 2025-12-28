import turtle

tortuga = turtle.Turtle()

tortuga.color("red")
tortuga.shape("turtle")

# it creates a screen object:
window = turtle.Screen()
window.bgcolor("black")

# to set the color mode to RGB:
# turtle.colormode(255)
# window.bgcolor(170,30,20)
window.title("Animation")

# to change the background pic:
# window.bgpic("file.gif")
# the file must be in the same folder
# this will tell us the current background pic:
# window.bgpic()
