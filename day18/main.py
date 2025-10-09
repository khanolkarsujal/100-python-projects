from turtle import Turtle , Screen


jimmy_the_turtle = Turtle()
jimmy_the_turtle.shape("turtle")
jimmy_the_turtle.color("red")



for i in range(4):

   jimmy_the_turtle.forward(100)
   jimmy_the_turtle.right(90)
 


screen = Screen()
screen.exitonclick()