import turtle

wn = turtle.Screen()
wn.bgcolor("blue")
tt = turtle.Turtle()
tt.shape("circle")
tt.color("white")
size = 10
tt.pensize(3)
tt.stamp()
ns = int(input("Number of sides: "))

for i in range(ns):
    tt.goto(0,0)
    tt.forward(200)
    tt.stamp()
    tt.right(360/ns)
    
wn.exitonclick()