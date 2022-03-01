"""had je složený ze 3 čtverečků a ty se pohybují - poslední čtverec se přesune na pozici druhého,
druhý čtverec na pozici prvního a první na pozici nula"""
from snake import Snake
import time
from turtle import Screen, _CFG
from food import Food
from score_board import ScoreBoard


screen = Screen()
# screen.setup(width=200, height=200)
screen.bgcolor("black")
screen.title("HAD")
screen.tracer(0) # automatický update je vypnutý

snake = Snake() #jakmile vytvoříme objekt, stane se vše, co je v __init__
food = Food()  #jakmile vytvoříme objekt, stane se vše, co je v __init__
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update() #aktualizuj obrazovku
    time.sleep(0.1)  # o 0.1 sekudndu pozdrží vykonání kódu - screen update
    snake.move()

    #detect the food collision - distance method - mezi dvěma objekty
    if snake.squares[0].distance(food) < 15:     #pozice od prvního čtverečku, food je 10x10
        food.refresh()
        snake.extend()
        score_board.score_up()

    #detect collision with wall
    if snake.squares[0].xcor() > 190 or snake.squares[0].xcor() < -190 or snake.squares[0].ycor() > 190 or snake.squares[0].ycor() < -190:
        game_is_on = False
        score_board.game_over()

    #detect collision with the tail
    #if the first square collide with any segment of the tail
    for square in snake.squares:  #pro každý čtvereček ze čtverečků z hadů
        if snake.squares[0].distance()





screen.exitonclick()