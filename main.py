from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "z")
screen.onkey(r_paddle.go_down, "s")
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_postion()
        
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_postion()
    
    
screen.exitonclick()