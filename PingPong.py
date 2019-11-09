import turtle

wn=turtle.Screen()
wn.title("My own turtles")
wn.bgcolor("blue")
wn.setup(width=700,height=400)
wn.tracer(0)

#padA
pad_A=turtle.Turtle()
pad_A.speed(10)
pad_A.shape("square")
pad_A.shapesize(stretch_wid=4,stretch_len=0.2)
pad_A.color("violet")
pad_A.penup()
pad_A.goto(-330,0)
pad_A.deaths=0

#PadB
pad_B=turtle.Turtle()
pad_B.speed(0)
pad_B.shape("square")
pad_B.shapesize(stretch_wid=4,stretch_len=0.2)
pad_B.color("red")
pad_B.penup()
pad_B.goto(330,0)
pad_B.deaths=0

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_wid=1,stretch_len=1)
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball.dx=0.2
ball.dy=0.2

def padA_up():
    y=pad_A.ycor()
    y+=20
    pad_A.sety(y)
def padA_down():
    y=pad_A.ycor()
    y-=20
    pad_A.sety(y)
def padA_left():
    if(pad_A.xcor()>-330):
        x=pad_A.xcor()
        x-=20
        pad_A.setx(x)
def padA_right():
    if(pad_A.xcor()<-300):
        x=pad_A.xcor()
        x+=20
        pad_A.setx(x)
def padB_up():
    y=pad_B.ycor()
    y+=20
    pad_B.sety(y)
def padB_down():
    y=pad_B.ycor()
    y-=20
    pad_B.sety(y)
def padB_left():
    if(pad_B.xcor()>300):
        x=pad_B.xcor()
        x-=10
        pad_B.setx(x)
def padB_right():
    if(pad_B.xcor()<330):
        x=pad_B.xcor()
        x+=10
        pad_B.setx(x)


def check_border():
    if(ball.xcor()<-350):
        ball.dx=ball.dx*(-1)
        pad_A.deaths=pad_A.deaths+1
    if(ball.xcor()>330):
        ball.dx=ball.dx*(-1)
        pad_B.deaths=pad_B.deaths+1
    if(ball.ycor()<-wn.canvheight/2-50 or ball.ycor()>wn.canvheight/2+50):
        ball.dy=-ball.dy

def checkPads():
    if(pad_A.distance(ball.xcor(),ball.ycor())<15):
        ball.dx=-ball.dx
        ball.dy=-ball.dy
    if(pad_B.distance(ball.xcor(),ball.ycor())<15):
        ball.dx=-ball.dx
        ball.dy=-ball.dy
    if(ball.distance(pad_A.xcor(),pad_A.ycor()+30)<15) or (ball.distance(pad_A.xcor(),pad_A.ycor()-30)<15):
        ball.dx=-ball.dx
        ball.dy=-ball.dy
    if(ball.distance(pad_B.xcor(),pad_B.ycor()+30)<15) or (ball.distance(pad_B.xcor(),pad_B.ycor()-30)<15):
        ball.dx=-ball.dx
        ball.dy=-ball.dy


#keyboard binding
wn.listen()
wn.onkeypress(padA_up,"w")
wn.onkeypress(padA_down,"s")
wn.onkeypress(padA_left,"a")
wn.onkeypress(padA_right,"d")
wn.onkeypress(padB_up,"8")
wn.onkeypress(padB_down,"2")
wn.onkeypress(padB_left,"4")
wn.onkeypress(padB_right,"6")

while True:
    wn.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    check_border()
    checkPads()
    #ball.pendown()
    wn.title("My own turtles. The left one died{0} times. The right one died{1} times.".format(pad_A.deaths,pad_B.deaths))


