import turtle
import math
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

# Paddle A
paddle_a = Paddle()
paddle_a.set_property()
paddle_a.goto(-350, 0)
# Paddle B
paddle_b = Paddle()
paddle_b.set_property()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2


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
        ball.dx = -ball.dx


