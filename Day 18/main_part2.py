import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########
for i  in range(10):
 
 tim.forward(10)
 tim.penup()
 tim.forward(10)
 tim.pendown()

screen = t.Screen()
screen.exitonclick()


