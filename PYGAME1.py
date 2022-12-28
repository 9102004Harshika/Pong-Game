import turtle
import winsound
win = turtle.Screen()
win.title("PONG GAME")
win.bgcolor("teal")
win.setup(width=800,height=600)
win.tracer(0)
#SCORE
SCORE_A=0
SCORE_B=0
#paddle a
paddle_A =turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("pink")
paddle_A.shapesize(stretch_wid=5,stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350,0)


#padle b
paddle_B =turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("pink")
paddle_B.shapesize(stretch_wid=5,stretch_len=1)
paddle_B.penup()
paddle_B.goto(350,0)

#ball
BALL =turtle.Turtle()
BALL.speed(0)
BALL.shape("square")
BALL.color("pink")
BALL.penup()
BALL.goto(0,0)
BALL.dx = 0.3
BALL.dy = -0.3
#PEN
pen=turtle.Turtle()
pen.speed(0)
pen.color("pink")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0  Player B :0",align="center",font=("Courier",24,"normal"))

#FUNCTIONS
def paddle_A_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)
def paddle_A_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)
def paddle_B_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)
def paddle_B_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)


#keyboard binding
win.listen()
win.onkeypress(paddle_A_up,"W")
win.onkeypress(paddle_A_down,"S")
win.onkeypress(paddle_B_up,"D")
win.onkeypress(paddle_B_down,"A")

#main game loop
while True:
    win.update()
    #move the ball
    BALL.setx(BALL.xcor()+BALL.dx)
    BALL.sety(BALL.ycor()+BALL.dy)
    #border check
    if BALL.ycor()> 290:
        BALL.sety(290)
        BALL.dy *= -1
        winsound.PlaySound("4379__noisecollector__pongblipg5.wav", winsound.SND_ASYNC)
    if BALL.ycor() < -290:
        BALL.sety(-290)
        BALL.dy *= -1
        winsound.PlaySound("4379__noisecollector__pongblipg5.wav", winsound.SND_ASYNC)
    if BALL.xcor() > 390:
        BALL.goto(0,0)
        BALL.dx *= -1
        SCORE_A += 1
        pen.clear()
        pen.write("Player A:{} Player B :{}".format(SCORE_A,SCORE_B), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("4379__noisecollector__pongblipg5.wav", winsound.SND_ASYNC)
    if BALL.xcor() < -390:
        BALL.goto(0,0)
        BALL.dx *= -1
        SCORE_B += 1
        pen.clear()
        pen.write("Player A:{} Player B :{}".format( SCORE_A, SCORE_B), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("4379__noisecollector__pongblipg5.wav",winsound.SND_ASYNC)
     #paddle and ball colli
    # sion
    if BALL.xcor()>340 and BALL.xcor() <350 and (BALL.ycor()<paddle_B.ycor()+ 50 and BALL.ycor()>paddle_B.ycor()-50):
        BALL.setx(340)
        BALL.dx *= -1
        winsound.PlaySound("4379__noisecollector__pongblipg5.wav", winsound.SND_ASYNC)
    if BALL.xcor() <-340 and BALL.xcor() > -350 and (
            BALL.ycor() < paddle_A.ycor() + 50 and BALL.ycor() > paddle_A.ycor() - 50):
        BALL.setx(-340)
        BALL.dx *= -1
        winsound.PlaySound("4379__noisecollector__pongblipg5.wav", winsound.SND_ASYNC)
