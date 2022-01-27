import random
from tkinter import *

root = Tk()
btns = []
bombs=[[False,False,False,False,False,False,False,False,False,False,False,False]]
def for_button_mine(x,y):
    pass#не чего не могу поделать:(
for i in range(10):
    a=[True,True,True,False,False,False,False,False,False,False]
    random.shuffle(a)
    a.insert(0,False)
    a.append(False)
    bombs.append(a)
bombs.append([False,False,False,False,False,False,False,False,False,False,False,False])
for i in bombs:
    print(i)

for i in range(10):
    step = {}
    for j in range(10):
        step[i, j] = {}
        step[i, j]['num'] = 0
        step[i, j]['кнопка'] = Button(root, width=2, height=1,command=lambda x=i,y=j:for_button_mine(x,y))
        step[i, j]['бомба'] = bombs[i+1][j+1]
        step[i, j]['координаты'] = [i, j]
        if i==0 or i==9 or j==0 or j==9:
            step[i, j]['видимость']=False
        else:
            step[i, j]['видимость'] = True
    btns.append(step)
for i in range(10):
    for j in range(10):
        if btns[i][i,j]['видимость']==True:
            btn=btns[i][i,j]['кнопка']
            btn.grid(row=i,column=j)

root.mainloop()