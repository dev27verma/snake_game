from turtle import Turtle

ALIGN = "center"
FONT = ("Aeril",24,"normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt","r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-10,260)
        self.update()

    def update(self):
        self.write(f"Score: {self.score}/Record: {self.high_score}", align=ALIGN, font=FONT)

    def highest_score(self):
        if self.score > self.high_score:
            self.high_score =  self.score
            with open("score.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0


    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}/Record: {self.high_score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGN, font=FONT)
