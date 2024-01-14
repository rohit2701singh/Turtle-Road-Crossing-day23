from turtle import Turtle

FONT = ("courier", 15, "underline")


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.player_level = 1
        self.level_update()

    def level_update(self):
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-245, 270)
        self.write(f"Level: {self.player_level}", align="center", font=FONT)

    def level_up(self):
        self.player_level += 1
        self.clear()
        self.level_update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)
