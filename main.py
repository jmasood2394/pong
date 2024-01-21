import time
from turtle import Screen

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600, startx=2848, starty=200)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)


r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)


is_active = True
while is_active:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # detect collision with right paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.paddle_bounce()

    if ball.xcor() > 370:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -370:
        ball.reset_position()
        score.r_point()


screen.exitonclick()
