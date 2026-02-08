import time
from turtle import Screen
from snake import  Snake

#set up the screen
window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("Snake Game")
window.tracer(0)

snake = Snake()

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











window.exitonclick()