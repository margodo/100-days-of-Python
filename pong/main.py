import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scorboard import Scoreboard

screen = Screen()
screen.screensize(800,600)
screen.bgcolor("black")
screen.title('pong')
screen.tracer(0)

paddle_1 = Paddle((350,0))
paddle_2 = Paddle((-350,0))

ball = Ball()

score_board = Scoreboard()

screen.listen()
screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")
screen.onkey(paddle_2.up, "w")
screen.onkey(paddle_2.down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset()
        score_board.l_point()
    if ball.xcor() < -380:
        ball.reset()
        score_board.r_point()





screen.exitonclick()