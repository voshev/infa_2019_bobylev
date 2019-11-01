from tkinter import *
import random
from random import randrange as rnd, choice
import time
import os
if os.path.isfile('results.txt'):
    print('file exist')
else:
    print('ni file')
root = Tk()
root.geometry('800x600')
score_1=0
score_2=0
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)


results = []

def load():
    global results
    file = open('results.txt','r')
    for i in file:
        results.append(i)
e = Entry(root, width=20)
def text():
    global e,score_1,score_2, results
    load()
    file = open('results.txt','w')
    for i in results:
        file.write(i)
    file.write(e.get()+':'+str(score_1)+','+str(score_2)+'\n')
    file.close()

b = Button(root, text="Enter", command=text)
#создает шарик в случайной точке
def new_ball():
    global x,y,r
    canv.create_text(50, 20, text=str(score_1),justify=CENTER, font="Verdana 14")
    x = random.randint(100,700)
    y = random.randint(100,500)
    r = random.randint(30,50)
    canv.create_oval(x-r,y-r,x+r,y+r,fill = 'red', width=0)
#удаляет предыдущий шарик и создает новый в квадрате a*a
def balling():
    global x,y,r
    canv.create_text(50, 20, text=str(score_1),justify=CENTER, font="Verdana 14")
    a = 10
    x = random.randint(x-a,x+a)
    y = random.randint(y-a,y+a)
    if x >= 700-r:
        x = random.randint(x-a,x)
    if x <= 100+r:
        x = random.randint(x,x+a)
    if y <= 100+r:
        y = random.randint(y,y+15)
    if y >= 500-r:
        y = random.randint(y-a,y)
    canv.create_oval(x-r,y-r,x+r,y+r,fill = 'red', width=0)
    root.after(1,balling)
#создает новый шарик в случайной точке
def new_ball_circle2():
    global x2,y2,r2
    canv.create_text(50, 20, text=str(score_1),justify=CENTER, font="Verdana 14")
    x2 = random.randint(100,700)
    y2 = random.randint(100,500)
    r2 = random.randint(30,50)
    canv.create_oval(x2-r2,y2-r2,x2+r2,y2+r2,fill = 'green', width=0)
#удаляет предыдущий шарик и создает новый в квадрате a*a
def balling_circle2():
    global x2,y2,r2
    a = 10
    x2 = random.randint(x2-a,x2+a)
    y2 = random.randint(y2-a,y2+a)
    if x2 >= 700-r2:
        x2 = random.randint(x2-a,x2)
    if x2 <= 100+r2:
        x2 = random.randint(x2,x2+a)
    if y2 <= 100+r2:
        y2 = random.randint(y2,y2+15)
    if y2 >= 500-r2:
        y2 = random.randint(y2-a,y2)
    canv.create_oval(x2-r2,y2-r2,x2+r2,y2+r2,fill = 'green', width=0)
    root.after(1,balling_circle2)
#обрабатывает щелчок мышки по шарикам
def click(event):
    global score_1,score_2,x,x1,x2, x_straight,y_straight
    if (event.x-x)**2+(event.y-y)**2<r**2:
        score_1+=1
        x=-100
        new_ball()
    print(score_1)
    if (event.x-x2)**2+(event.y-y2)**2<r2**2:
        score_1+=1
        x2=-100
        new_ball_circle2()
    print(score_1)
    if (event.x-x1)**2+(event.y-y1)**2<r1**2:
        score_2+=1
        x1=-100
        new_ball2()
    print(score_2)
    if (event.x-x_straight)**2 + (event.y-y_straight)**2 < r_straight**2:
        score_1+=1
        x_straight=-100
        new_ball_straight()
#создает квадрат в случайной точке
def new_ball2():
    global x1,y1,r1
    canv.create_text(50, 20, text=str(score_1),justify=CENTER, font="Verdana 14")
    x1 = random.randint(100,700)
    y1 = random.randint(100,500)
    r1 = random.randint(30,50)
    canv.create_rectangle(x1-r1,y1-r1,x1+r1,y1+r1,fill = 'black', width=0)
#удаляет предыдущий квадрат и создает новый в квадрате a*a
def balling2():
    global x1,y1,r1
    canv.create_text(50, 40, text=str(score_2),justify=CENTER, font="Verdana 14")
    a = 10
    x1 = random.randint(x1-a,x1+a)
    y1 = random.randint(y1-a,y1+a)
    if x1 >= 700-r1:
        x1 = random.randint(x1-a,x1)
    if x1 <= 100+r1:
        x1 = random.randint(x1,x1+a)
    if y1 <= 100+r1:
        y1 = random.randint(y1,y1+a)
    if y1 >= 500-r1:
        y1 = random.randint(y1-15,y1)
    canv.create_rectangle(x1-r1,y1-r1,x1+r1,y1+r1,fill = 'black', width=0)
    root.after(1,balling2)
#шарик двигающийся прямо
def new_ball_straight():
    global x_straight,y_straight,r_straight
    x_straight = random.randint(200,600)
    y_straight = random.randint(200,400)
    r_straight = random.randint(30,50)
    canv.create_oval(x_straight-r_straight,y_straight-r_straight,x_straight+r_straight,y_straight+r_straight,fill = 'blue', width=0)
#удаляет предыдущий шарик и создает новый в квадрате a*a
vx=random.randint(1,10)
vy=random.randint(1,10)
def balling_straight():
    global x_straight,y_straight,r_straight,vx,vy
    canv.delete(ALL)
    x_straight+=vx
    y_straight+=vy
    if (x_straight >= 700-r_straight) or (x_straight <= 100+r_straight):
        vx=-vx
    if (y_straight <= 100+r_straight) or (y_straight >= 500-r_straight):
        vy=-vy
    canv.create_oval(x_straight-r_straight,y_straight-r_straight,x_straight+r_straight,y_straight+r_straight,fill = 'blue', width=0)
    root.after(16,balling_straight)

new_ball()
balling()

new_ball_circle2()
balling_circle2()

new_ball2()
balling2()

new_ball_straight()
balling_straight()

e.pack()
b.pack()

canv.bind('<Button-1>', click)

mainloop()
