#Simple Pong game
#Sophia Tran

import turtle

#create a window

wn = turtle.Screen()
wn.title("Pong by Sophia")
wn.bgcolor("black")
wn.setup(width = 800, height =600)
wn.tracer(0) #stops window from updating

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() #don't draw lines
paddle_a.goto(-350,0)



# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() #don't draw lines
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0) #speed of animation
ball.shape("circle")
ball.color("white")
ball.penup() #don't draw lines
ball.goto(0,0)
ball.dx = 0.2 #dx like change in gradient
ball.dy = -0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0        Player B: 0", align="center", font=("Comic Sans", 24, "italic"))

#Functions
def paddle_a_up():
    y = paddle_a.ycor() 
    y += 30
    paddle_a.sety(y) 

def paddle_a_down():
    y = paddle_a.ycor() 
    y -= 30
    paddle_a.sety(y) 

def paddle_b_up():
    y = paddle_b.ycor() 
    y += 30
    paddle_b.sety(y) 

def paddle_b_down():
    y = paddle_b.ycor() 
    y -= 30
    paddle_b.sety(y) 

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}        Player B: {}".format(score_a, score_b), align="center", font=("Comic Sans", 24, "italic"))
    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A: {}        Player B: {}".format(score_a, score_b), align="center", font=("Comic Sans", 24, "italic"))

    # Paddle and ball collisions
    if ball.xcor() >= 345 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60):
        ball.setx(345)
        ball.dx *= -1

    if ball.xcor() <= -345 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
        ball.setx(-345)
        ball.dx *= -1
    
    # Paddle off the screen
    if paddle_b.ycor() + 60 > 300:
        paddle_b.sety(250)
    elif paddle_b.ycor() - 60 < -300:
        paddle_b.sety(-250)

    if paddle_a.ycor() + 60 > 300:
        paddle_a.sety(250)
    elif paddle_a.ycor() - 60 < -300:
        paddle_a.sety(-250)