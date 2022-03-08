from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as number:
            self.high_score = int(number.read())
        self.hideturtle()
        self.goto(x=0, y=180)
        self.color("white")
        self.update_scoreboard()

    def score_up(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as number:
                number.write(str(self.high_score))
        self.score = 0  #musíme znovu vynulovat před další hrou
        self.update_scoreboard()



    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write("GAME OVER", align="left", font=FONT)