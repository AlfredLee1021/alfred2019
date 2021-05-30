import turtle
import math
import os
from typing import Tuple
class Paddle(turtle.Turtle):

    def paddle_up(self):
        self.sety(self.ycor() + 20)
    def paddle_down(self):
        self.sety(self.ycor() - 20)
    def set_property(self):
        self.speed(0)
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()



wn = turtle.Screen()
wn.title('Pong by @Alfred')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)
point_a = 0
point_b = 0

# Paddle A
paddle_a = Paddle()
paddle_a.set_property()
paddle_a.goto(-350, 0)
paddle_a.fillcolor("green")

# Paddle B
paddle_b = Paddle()
paddle_b.set_property()
paddle_b.goto(350, 0)
paddle_b.fillcolor("red")

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

#pen
pen = Paddle()
pen.set_property()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {} Player B: {}".format(point_a, point_b), align='center', font=('Courier', 24, 'normal'))


# Keybooard binding
wn.listen()
wn.onkeypress(paddle_a.paddle_up, 'w')
wn.onkeypress(paddle_a.paddle_down, "s")
wn.onkeypress(paddle_b.paddle_up, 'Up')
wn.onkeypress(paddle_b.paddle_down, "Down")

# Main game loop
while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if abs(ball.ycor()) > 290:
        ball.sety(290 if ball.ycor() > 0 else -290)
        ball.dy = -ball.dy
    if abs(ball.xcor()) > 390:
        ball.setx(390 if ball.xcor() > 0 else -390)
        if ball.xcor() > 0:
            point_a += 1 
            pen.clear()
            pen.write(f"Player A: { point_a} Player B: {point_b}", align='center', font=('Courier', 24, 'normal'))
 
        else:
            point_b += 1
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(point_a, point_b), align='center', font=('Courier', 24, 'normal'))
 
        ball.dx = -ball.dx
      
    if abs(ball.xcor() - paddle_a.xcor()) <= 15 and abs(ball.ycor()- paddle_a.ycor()) < 50:
        ball.dx = -ball.dx
    if abs(ball.xcor() - paddle_b.xcor()) <= 15  and abs(ball.ycor()- paddle_b.ycor()) < 50:
        ball.dx = -ball.dx

