import turtle
import random
import sys

print(sys.version)

tao = turtle.Pen() #Use Pen
tao.color("blue")
tao.shape('turtle') #Change to Turtle

vtimes = 0

def Rectangle(times):
    '''วาดรูปสี่เหลี่ยม'''
    for i in range(times):
        for i in range(4):
            tao.forward(100)
            tao.left(90)
        tao.left(25)

def Triangle(times):
    '''วาดรูปสามเหลี่ยม'''
    for i in range(times):
        tao.forward(100)
        tao.left(120)
        tao.forward(100)
         
        tao.left(120)
        tao.forward(100)
        tao.left(25)

def Circle(times,r):
    '''วาดรูปวงกลม'''
    for i in range(times):
        tao.circle(r)
        tao.left(35)
        #tColor = ['red', 'yellow', 'black']
        #taoColor = random.choice(tColor)
        #tao.color(taoColor)
        
def taoGo(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()
    
Triangle(25)
#taoGo(200,200)
#Rectangle()
taoGo(200,200)
Circle(20,50)
taoGo(-200,-200)
Rectangle(25)
#taoGo(200,-200)
#Circle(10,50)
#taoGo(-200,200)
#Circle(10,50)
#tao.home()

