import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tt = turtle.Turtle()
tt.shape("turtle")
tt.color("blue")
size = 10
tt.pensize(3)
tt.stamp()

for i in range(12):
    tt.right(30)
    tt.goto(0,0)
    tt.penup()
    tt.forward(100)
    tt.pendown()
    tt.forward(10)
    tt.penup()
    tt.forward(20)
    tt.stamp()
    
wn.exitonclick()