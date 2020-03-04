import turtle

wn = turtle.Screen()
tt = turtle.Turtle()
n = int(input("Number of sides: "))
c = int(input("Length of the side: "))
bc = input("Border color: ")
fc = input("Fill Color: ")
tt.pensize(5)
tt.color(bc)

tt.fillcolor(fc)
tt.begin_fill()
for i in range (n):
    tt.forward(c)
    tt.left(360/n)
tt.end_fill()

wn.exitonclick()