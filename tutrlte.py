import turtle
"""graph=turtle.Turtle()
graph.shape()
graph.shape("turtle")
graph.color("green","blue")
graph.forward(200)
"""
"""win=turtle.Screen()
win.bgcolor("black")
t=turtle.Turtle()
t.color("white")
t.forward(100)
t.right(200)
t.forward(300)
"""
"""t=turtle.Turtle()
t.speed(1)
t.fillcolor("red")
for i in range(4):
    t.forward(200)
    t.left(90)
"""
"""star = turtle.Turtle()
star.right(75)
star.forward(100)
for i in range(4):
    star.right(144)
    star.forward(100)
turtle.done()"""
"""for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
turtle.exitonclick()"""
"""t=turtle.Turtle()
t.up()
t.goto(0,-50)
t.down()
t.begin_fill()
t.fillcolor("green")
t.circle(50)
t.end_fill()
turtle.done()"""
tu=turtle.Turtle()
tu.speed(0)
list1 = ["red","green","blue","orange","green"]
for i in range(200):
    tu.color(list1[i%5])
    tu.pensize(i/5)
    tu.forward(i)
    tu.left(59)