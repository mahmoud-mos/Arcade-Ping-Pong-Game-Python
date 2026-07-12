import turtle

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_SPEED = 25
BALL_DX = 2.5
BALL_DY = 2.5

class Paddle(turtle.Turtle):
    def __init__(self, x, color):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, 0)

    def move_up(self):
        y = self.ycor()
        if y < 250:
            self.sety(y + PADDLE_SPEED)

    def move_down(self):
        y = self.ycor()
        if y > -250:
            self.sety(y - PADDLE_SPEED)

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = BALL_DX
        self.dy = BALL_DY

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score_left = 0
        self.score_right = 0
        self.update_display()

    def update_display(self):
        self.clear()
        self.write(f"Player A: {self.score_left}  Player B: {self.score_right}", 
                   align="center", font=("Courier", 24, "normal"))

    def increment_left(self):
        self.score_left += 1
        self.update_display()

    def increment_right(self):
        self.score_right += 1
        self.update_display()

class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Ping Pong")
        self.screen.bgcolor("black")
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.tracer(0)

        self.paddle_left = Paddle(-350, "red")
        self.paddle_right = Paddle(350, "blue")
        self.ball = Ball()
        self.scoreboard = ScoreBoard()

        self.screen.listen()
        self.screen.onkeypress(self.paddle_left.move_up, "w")
        self.screen.onkeypress(self.paddle_left.move_down, "s")
        self.screen.onkeypress(self.paddle_right.move_up, "Up")
        self.screen.onkeypress(self.paddle_right.move_down, "Down")

    def run(self):
        self.update()
        self.screen.mainloop()

    def update(self):
        self.screen.update()
        self.ball.move()

        # Border Collision
        if self.ball.ycor() > 290 or self.ball.ycor() < -290:
            self.ball.dy *= -1

        # Goal Logic
        if self.ball.xcor() > 390:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            self.scoreboard.increment_left()

        if self.ball.xcor() < -390:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            self.scoreboard.increment_right()

        # Paddle Collision
        if (340 < self.ball.xcor() < 350) and (self.paddle_right.ycor() + 50 > self.ball.ycor() > self.paddle_right.ycor() - 50):
            self.ball.setx(340)
            self.ball.dx *= -1

        if (-350 < self.ball.xcor() < -340) and (self.paddle_left.ycor() + 50 > self.ball.ycor() > self.paddle_left.ycor() - 50):
            self.ball.setx(-340)
            self.ball.dx *= -1

        self.screen.ontimer(self.update, 10)

if __name__ == "__main__":
    game = Game()
    game.run()
