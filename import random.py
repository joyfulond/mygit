import random
from turtle import *
from time import time 


newBodyPos=()
body_Snake=[]
apple=Turtle()
scoreText=Turtle()
score=-1
speed=0.1
gameover= Turtle()
gameover.hideturtle()


def set_Apple():
    global apple,score
    
    apple.goto(random.randint(-14,14)*20,random.randint(-14,14)*20)
    score+=1
    scoreText.clear()
    scoreText.write("score :%d"%score,False,'center',font=("consolas",20))
    
def Setup():
    hideturtle()
    bgcolor("green")
    Screen().setup(600,600)
    Screen().title("Snake Game")
    
    for i in [(0,0),(-20,0),(-40,0)]:
        s=Turtle()
        s.shape("square")
        s.up()
        s.goto(i)
        s.speed(0)
        body_Snake.append(s)
    body_Snake[0].color("blue")
    
    apple.up()
    apple.speed(0)
    apple.color("red")
    apple.shape("square")
    
    scoreText.hideturtle()
    scoreText.speed(0)
    scoreText.up()
    scoreText.goto(200,200)
    
    onkeypress(up,"Up")
    onkeypress(right,"Right")
    onkeypress(left,"Left")
    onkeypress(down,"Down")
    set_Apple()
    
def make_body():
    s=Turtle()
    s.shape("square")
    s.up()
    s.speed(0)
    s.goto(newBodyPos)
    body_Snake.append(s)
    
def isSameList(a,b):
    for i in range(len(a)):
        if(a[i]!=b[i]):
            return 0
    return 1

def move():
    global speed, newBodyPos
    newBodyPos=body_Snake[len(body_Snake)-1].pos()
    for i in range(len(body_Snake)-1,0,-1):
      body_Snake[i].goto(body_Snake[i-1].pos())
    body_Snake[0].forward(20)
    head=body_Snake[0].pos()
    b=list(head)
    a=list(apple.pos())
    b[0]=round(int(b[0]),-1)
    b[1]=round(int(b[1]),-1)
    a[0]=round(int(a[0]),-1)
    a[1]=round(int(a[1]),-1)
        
    if(isSameList(a,b)):    
        speed-=0.015
        set_Apple()
        make_body()
        
    for i in body_Snake[1:]:
        if(head==i.pos()):
            gameover.write("GAME OVER ...(종료하려면 엔터)",font=("consolas",20))
            input()
            exit(1)
    if(-300>=b[0] or -300>=b[1] or b[0]>=300 or b[1]>=300):
        gameover.write("GAME OVER ...(종료하려면 엔터)",font=("consolas",20))
        input()
        exit(1)

def down():
    if(body_Snake[0].heading()!=90):
       body_Snake[0].setheading(270)
def up():
    if(body_Snake[0].heading()!=270):
        body_Snake[0].setheading(90)
def right():
    if(body_Snake[0].heading()!=180):
        body_Snake[0].setheading(0)
        
def left():
    if(body_Snake[0].heading()!=0):
        body_Snake[0].setheading(180)

def main():
  while(True):
    start=time()
    while(time()-start<speed):
      pass
    move()
    
Setup()
listen()
main()