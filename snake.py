import turtle
import time
import random
delay=0.1
score=0
highscore=0
# background
wn =turtle.Screen()
wn.title("Snake game by @pj")
wn.bgcolor("green")
wn.setup(width=600,height=600)
#tracer is used to turn off the animation
wn.tracer(0)


# snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# snake food to eat
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)



segments = []


# pen

pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0" ,align="center",font=("Courier",24,"normal"))
# create a function to move the snake by the user
def go_up():
    if head.direction != "down":

        head.direction="up"

def go_down():

      if head.direction != "up":

            head.direction="down"

def go_right():
      if head.direction != "left":

             head.direction="right"

def go_left():
      if head.direction != "right":

           head.direction="left"

# creat a function to move
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y + 20)

    if head.direction=="down":
        y=head.ycor()
        head.sety(y - 20)

    if head.direction=="right":
        x=head.xcor()
        head.setx(x + 20)

    if head.direction=="left":
        x=head.xcor()
        head.setx(x - 20)

# keyword press keys
wn.listen()
wn.onkeypress(go_up,"w"or "up")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_right,"d")
wn.onkeypress(go_left,"a")

while True:
    wn.update()

    if head.xcor()>290 or head.xcor()< -290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction ="stop"

        for segment in segments:
            segment.goto(1000,1000 )

        segments.clear()

        score=0
        pen.clear()
        pen.write("Score: {} High Score {}".format(score,highscore),align="center",font=("Courier",24,"normal"))
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
     #increase score
        score += 10

        if score>highscore:
            highscore=score
            pen.clear()
            pen.write("Score: {}  High Score {} ".format(score,highscore),align="center",font=("Courier",24,"normal"))
    for index in range(len(segments)-1,0,-1):

        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    if len(segments)>0:

        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)


    move()

    for segment in segments:
        if segment.distance(head)<20:

             time.sleep(1)
             head.goto(0,0)
             head.direction ="stop"

             for segment in segments:
                  segment.goto(1000,1000)

             segments.clear()


    time.sleep(delay)
wn.mainloop()
