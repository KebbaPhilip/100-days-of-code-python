import time
from turtle import Screen
from scoreboard import Scoreboard
from snake import  Snake
from food import Food

#set up the screen
window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("Snake Game")
window.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

window.listen()
window.onkey(snake.up, "Up")
window.onkey(snake.down, "Down")
window.onkey(snake.left, "Left")
window.onkey(snake.right, "Right")


game_on = True
while game_on:
    window.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    #Detect head collision with body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()












window.exitonclick()