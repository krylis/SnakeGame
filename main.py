import turtle

screen = turtle.Screen()
screen.screensize(600, 800, "grey")

# Create player controlled ship
player = turtle.Turtle()
player.shape("triangle")
player.left(90)
player.penup()
player.goto(0, -350)

# Methods for moving the ship
def left():
    player.goto(player.xcor() - 10, -350)


def right():
    player.goto(player.xcor() + 10, -350)


screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()

screen.mainloop()
