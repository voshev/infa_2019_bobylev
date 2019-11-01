import	random
from	tkinter	import*
import	math
import	time

root=Tk()
fr=Frame(root)
root.geometry('800x600')
canv=Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

n = 5

a = [[random.randint(0, 799), random.randint(0,599)], [random.randint(0,799), random.randint(0,599)], [random.randint(0,799), random.randint(0,599)]]

for i in range(3, n):
	a.append([random.randint(0, 799), random.randint(0,599)])

x = random.randint(0, 799)
y = random.randint(0, 599)

b = []
for i in range(0, n):
	b.append([400+250*math.cos(2*i*math.pi/n), 300-250*math.sin(2*i*math.pi/n)])

canv.create_oval(b[0][0], b[0][1], b[0][0], b[0][1], fill='black', width=0)
canv.create_oval(b[1][0], b[1][1], b[1][0], b[1][1], fill='black', width=0)
canv.create_oval(b[2][0], b[2][1], b[2][0], b[2][1], fill='black', width=0)
for i in range(3, n):
	canv.create_oval(b[i][0], b[i][1], b[i][0], b[i][1], fill='black', width=0)

def draw():
	global x, y, n
	for i in range(0,100):
		canv.create_oval(x, y, x, y, fill='black', width=0)
		tmp = random.randint(0,n-1)
		x = (x+b[tmp][0])/2
		y = (y+b[tmp][1])/2
	root.after(16, draw)

draw()
mainloop()
