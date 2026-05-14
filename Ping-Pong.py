import turtle

# Window Setup
wind = turtle.Screen()
wind.title("Ping Pong")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0) 

# Game State 
score_left = 0
score_right = 0

# Game Objects 

# Paddle Left (Red)
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("red") 
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350, 0)

# Paddle Right (Blue)
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("blue") 
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.penup()
paddle_right.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white") 
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25  # Horizontal Speed
ball.dy = 0.25  # Vertical Speed

# Score Display
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions 

def move_paddle(paddle, pixels):
    """Handles movement for both paddles with boundary checking."""
    y = paddle.ycor()
    y += pixels
    if 250 > y > -250: # Keeps paddles from going off-screen
        paddle.sety(y)

def update_score():
    """Refreshes the score display."""
    pen.clear()
    pen.write(f"Player A: {score_left}  Player B: {score_right}", align="center", font=("Courier", 24, "normal"))

# Keyboard Bindings
wind.listen()
# Left Paddle: W / S
wind.onkeypress(lambda: move_paddle(paddle_left, 25), "w")
wind.onkeypress(lambda: move_paddle(paddle_left, -25), "s")
# Right Paddle: Up / Down Arrows
wind.onkeypress(lambda: move_paddle(paddle_right, 25), "Up")
wind.onkeypress(lambda: move_paddle(paddle_right, -25), "Down")

# --- Main Game Loop ---
while True:
    wind.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Collision (Top/Bottom)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Goal Logic (Left/Right)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1 
        score_left += 1
        update_score()
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_right += 1
        update_score()
        
    # Paddle & Ball Collision Logic
    # Right Paddle Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and \
       (paddle_right.ycor() + 50 > ball.ycor() > paddle_right.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    # Left Paddle Collision
    if (ball.xcor() < -340 and ball.xcor() > -350) and \
       (paddle_left.ycor() + 50 > ball.ycor() > paddle_left.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
