from graph import*
import math
width=1000
height=600
windowSize(width,height)

"""Рисует темно-синий прямоугольник"""
brushColor(68,35,223)
penSize(400)
penColor(68,35,223)
line(0,250,1000,250)
"""Рисует светло-синий прямоугольник"""
brushColor(161,245,255)
penSize(420)
penColor(161,245,255)
line(0,0,1000,0)

def umbrella(size,x_center,y_center, size_width):
    penSize(1*size)
    """Рисует шляпку зонтика"""
    brushColor(244,81,81)
    penColor(244,81,81)
    polygon([(x_center-size_width*40*size,y_center),(x_center,y_center-40*size),(x_center+size_width*40*size,y_center),(x_center-size_width*40*size,y_center)])
    """Рисует линии на шляпке зонтика"""
    brushColor(181,60,60)
    penColor(181,60,60)
    line(x_center,y_center-40*size,x_center+10*size_width*size,y_center)
    line(x_center,y_center-40*size,x_center+20*size_width*size,y_center)
    line(x_center,y_center-40*size,x_center+30*size_width*size,y_center)
    line(x_center,y_center-40*size,x_center-10*size_width*size,y_center)
    line(x_center,y_center-40*size,x_center-20*size_width*size,y_center)
    line(x_center,y_center-40*size,x_center-30*size_width*size,y_center)
    """Рисует ножку зонтика"""
    penSize(0.1*size)
    brushColor(244,81,81)
    penColor(181,60,60)
    rectangle(x_center-2*size_width*size,y_center-40*size,x_center+2*size_width*size,y_center)
    penSize(6*size)
    brushColor(227,130,25)
    penColor(227,130,25)
    line(x_center , y_center , x_center , y_center+120*size)

def sun(r_max,r_min,x_center,y_center,n):
    a=[]
    for i in range (0,n):
        x=x_center+math.cos(2*math.pi*i/n)*r_max
        y=y_center+math.sin(2*math.pi*i/n)*r_max
        a.append((x , y))
        x=x_center+math.cos(2*math.pi*i/n+math.pi/n)*r_min
        y=y_center+math.sin(2*math.pi*i/n+math.pi/n)*r_min
        a.append((x , y))
    brushColor('yellow')
    penColor('yellow')
    penSize(1)
    polygon(a)

def wave(width,height,n,k,screen_height):
    a=[]
    for i in range (0,width):
        x=i
        y=height+k*math.sin(0.02*math.pi*i*n)
        a.append((x , y))
    a.append((width, screen_height-1))
    a.append((0, screen_height-1))
    brushColor('yellow')
    penColor('yellow')
    penSize(1)
    polygon(a)
def clouds(x_center,y_center,k_x,k_y,i):
    brushColor('white')
    penColor('black')
    penSize(1)
    ellips(x_center-25*k_x,y_center+5*k_y,x_center-15*k_x,y_center-5*k_y)
    ellips(x_center+5*k_x,y_center-25*k_y,x_center-5*k_x,y_center-15*k_y)
    ellips(x_center-45*k_x,y_center-12*k_y,x_center-35*k_x,y_center-2*k_y)
    ellips(x_center-15*k_x,y_center-12*k_y,x_center-5*k_x,y_center-2*k_y)
    ellips(x_center+20*k_x,y_center-12*k_y,x_center+10*k_x,y_center-2*k_y)
    ellips(x_center+15*k_x,y_center+3*k_y,x_center+5*k_x,y_center-7*k_y)
    ellips(x_center+25*k_x,y_center-12*k_y,x_center+15*k_x,y_center-2*k_y)
def boat(x_center,y_center,size):
    """Рисует четверть окружности лодки"""
    brushColor(186,80,5)
    penColor('black')
    penSize(1*size)
    circle(x_center-75*size,y_center-10*size,20*size)
    brushColor(68,35,223)
    penColor(68,35,223)
    penSize(21*size)
    line(x_center-105*size,y_center-20*size,x_center-45,y_center-20*size)
    """Рисует прямоугольник лодки"""
    brushColor(186,80,5)
    penSize(1*size)
    penColor('black')
    rectangle(x_center-75*size,y_center-10*size,x_center+105*size,y_center+10*size)
    """Рисует треугольник лодки"""
    penColor('black')
    polygon([(x_center+105*size,y_center-10*size),(x_center+155*size,y_center-10*size),(x_center+105*size,y_center+10*size),(x_center+105*size,y_center-10*size)])
    """Рисует окружность на лодке"""
    brushColor('white')
    penColor('black')
    penSize(3*size)
    circle(x_center+115*size,y_center-2*size,5*size)
    """Рисует мачту"""
    brushColor('black')
    penColor('black')
    penSize(4*size)
    line(x_center-35*size,y_center-10*size,x_center-35*size,y_center-110*size)
    """Рисует парус"""
    brushColor(222,213,153)
    penColor('black')
    penSize(1*size)
    polygon([(x_center-35*size,y_center-110*size),(x_center+25*size,y_center-60*size),(x_center-15*size,y_center-60*size),(x_center-35*size,y_center-110*size)])
    polygon([(x_center-35*size,y_center-10*size),(x_center+25*size,y_center-60*size),(x_center-15*size,y_center-60*size),(x_center-35*size,y_center-10*size)])


clouds(100,100,3,3,1)
boat(600,290,2)
boat(350,250,1)
wave(width,height*0.6,0.6,15,height)
umbrella(2,width*0.2,height*0.5,1.5)
umbrella(1,width*0.4,height*0.6,1)
sun(80,65,width*0.9,height*0.15,50)
run()
