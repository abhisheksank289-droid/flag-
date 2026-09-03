import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Flag stripes
def rectangle(color, x, y, width, height):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

rectangle("orange", -200, 150, 400, 80)
rectangle("white", -200, 70, 400, 80)
rectangle("green", -200, -10, 400, 80)

# Ashoka Chakra
t.penup()
t.goto(0, 25)
t.setheading(0)
t.pendown()
t.pencolor("blue")
t.circle(40)

# Chakra spokes
for _ in range(24):
    t.penup()
    t.goto(0, 65)
    t.pendown()
    t.goto(0, 25)
    t.right(15)

# Flag pole
t.pencolor("black")
t.penup()
t.goto(-200, 150)
t.pendown()
t.goto(-200, -150)

turtle.done()