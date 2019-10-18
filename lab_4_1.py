from tkinter import *
import random
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')
i=0
j=0
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

#создает шарик в случайной точке
def new_ball():
    global x,y,r
    canv.create_text(50, 20, text=str(i),justify=CENTER, font="Verdana 14")
    x = random.randint(100,700)
    y = random.randint(100,500)
    r = random.randint(30,50)
    canv.create_oval(x-r,y-r,x+r,y+r,fill = 'red', width=0)
#удаляет предыдущий шарик и создает новый в квадрате a*a
def balling():
    global x,y,r
    canv.create_text(50, 20, text=str(i),justify=CENTER, font="Verdana 14")
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
    canv.create_text(50, 20, text=str(i),justify=CENTER, font="Verdana 14")
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
    global i,j,x,x1,x2
    if (event.x-x)**2+(event.y-y)**2<r**2:
        i+=1
        x=-100
        new_ball()
    print(i)
    if (event.x-x2)**2+(event.y-y2)**2<r2**2:
        i+=1
        x2=-100
        new_ball_circle2()
    print(i)
    if (event.x-x1)**2+(event.y-y1)**2<r1**2:
        j+=1
        x1=-100
        new_ball2()
    print(j)
#создает квадрат в случайной точке
def new_ball2():
    global x1,y1,r1
    canv.create_text(50, 20, text=str(i),justify=CENTER, font="Verdana 14")
    x1 = random.randint(100,700)
    y1 = random.randint(100,500)
    r1 = random.randint(30,50)
    canv.create_rectangle(x1-r1,y1-r1,x1+r1,y1+r1,fill = 'black', width=0)
#удаляет предыдущий квадрат и создает новый в квадрате a*a
def balling2():
    global x1,y1,r1
    canv.delete(ALL)
    canv.create_text(50, 40, text=str(j),justify=CENTER, font="Verdana 14")
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

new_ball()
balling()

new_ball_circle2()
balling_circle2()

new_ball2()
balling2()


canv.bind('<Button-1>', click)
mainloop()
