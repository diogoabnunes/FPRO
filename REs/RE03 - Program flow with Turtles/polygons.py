import turtle
wn = turtle.Screen()
tt = turtle.Turtle()

for i in range(4):
    tt.forward(100)
    tt.left(360/4)
    
for i in range(3):
    tt.forward(100)
    tt.left(360/3)

for i in range(6):
    tt.forward(100)
    tt.left(360/6)

for i in range(8):
    tt.forward(100)
    tt.left(360/8)
    
wn.exitonclick()

#import turtle
#
#wn = turtle.Screen()
#tt = turtle.Turtle()
#for i in [4,3,6,8]:
#    for j in range(i):
#        tt.forward(50)
#        tt.left(360/i)
#
#wn.exitonclick()