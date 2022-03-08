from turtle import Turtle
import random
"""chceme, aby Food class zdědila vše z Turtle class"""
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  #standartně je to 20x20 - tímto to zmenšíme na polovinu
        self.color("pink")
        self.speed("fastest") #abysme nemuseli sledovat jak se tvoří, jak se přesunuje na jiné místo
        self.refresh()

    def refresh(self): #když se foodu dotkne had, tak změní pozici
        rand_x = random.randint(-180, 180)  # aby to nebylo přes celou obrazovku -250, 250
        rand_y = random.randint(-180, 180)
        self.goto(x=rand_x, y=rand_y)

