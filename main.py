from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
#from highscores import HighScore
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
# highscore = HighScore()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


def snake_game():
    # highscore.scores()
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
            #Dectect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

            #DETECT COLLISION WITH WALL
        if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            scoreboard.reset()
            snake.reset()
            # scoreboard.add_high_score()
            # if scoreboard.score > highscore.scores:
            #     highscore.scores += scoreboard.score
            # scoreboard.reset()
            # snake_game()


            #DETECT COLLISION WITH TAIL
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()
                # scoreboard.add_high_score()
                # if scoreboard.score > highscore.scores:
                #     highscore.scores += scoreboard.score

                #snake_game()






    screen.exitonclick()

snake_game()