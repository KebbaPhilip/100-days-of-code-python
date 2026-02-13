import time
from turtle import Screen
from ball import Ball
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")

screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.paddle_up, "Up")
screen.onkey(r_paddle.paddle_down, "Down")
screen.onkey(l_paddle.paddle_up, "w")
screen.onkey(l_paddle.paddle_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect collision with wall ycor
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

    #detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect if right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce_x()

    #detect if left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        ball.bounce_x()





screen.exitonclick()