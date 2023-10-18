from turtle import *

speed(8)
pensize(3)
Screen().bgcolor("white")

h = 150
w = 1000

up()
goto(-500, 200)
down()

# Black color
begin_fill()
for _ in range(2):  
    forward(w)
    left(90)
    forward(h)
    left(90)
end_fill()

# White color
color("#fff")
right(90)
forward(h)

# Green color
color("green")
begin_fill()
for _ in range(2):
    forward(h)
    left(90)
    forward(w)
    left(90)
end_fill()

# Red color
color("red")
begin_fill()
forward(h)
forward(-h * 3)
left(60)
forward(h * 3)
right(120)
forward(h * 3)
end_fill()

# Border
color("#000")
pensize(1)
right(120)

for _ in range(2):
    forward(h * 3)
    right(90)
    forward(w)
    right(90)

hideturtle()
done()
