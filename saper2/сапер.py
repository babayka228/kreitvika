import random
from tkinter import *

root = Tk()
btns = []
cells = [[i, j] for i in range(1, 9) for j in range(1, 9)]
random.shuffle(cells)

bombs=[[False, False, False, False,False,False, False, False, False,False] for _ in range(10)]
def for_button_mine(x,y):
    global btns
    print(x,y)
    if btns[x][x,y]['видимость']==True:
        
        btns[x][x,y]['нажата?']=True
        btns[x][x,y]['кнопка'].config(state='disabled')
        mins=0
        if btns[x][x,y]['бомба']==True:
            for i in range(10):
                for j in range(10):
                    if btns[i][i,j]['бомба']==True:
                        btns[i][i,j]['кнопка'].config(state='disabled',background="#f00")
                    else:
                        btns[i][i,j]['кнопка'].config(state='disabled')
        if btns[x][x,y]['бомба']==False:
            if btns[x-1][x-1,y-1]['бомба']==True:
                mins+=1
            if btns[x][x,y-1]['бомба']==True:
                mins+=1
            if btns[x+1][x+1,y-1]['бомба']==True:
                mins+=1
            if btns[x+1][x+1,y]['бомба']==True:
                mins+=1
            if btns[x+1][x+1,y+1]['бомба']==True:
                mins+=1
            if btns[x][x,y+1]['бомба']==True:
                mins+=1
            if btns[x-1][x-1,y+1]['бомба']==True:
                mins+=1
            if btns[x-1][x-1,y]['бомба']==True:
                mins+=1
            if mins!=0:
                btns[x][x,y]['кнопка'].config(text=mins)
            elif mins==0:
                if btns[x][x-1,y-1]['нажата?']==False:
                    for_button_mine(x-1,y-1)
                if btns[x][x,y-1]['нажата?']==False:
                    for_button_mine(x,y-1)
                if btns[x][x+1,y-1]['нажата?']==False:
                    for_button_mine(x+1,y-1)
                if btns[x][x+1,y]['нажата?']==False:
                    for_button_mine(x+1,y)
                if btns[x][x+1,y+1]['нажата?']==False:
                    for_button_mine(x+1,y+1)
                if btns[x][x,y+1]['нажата?']==False:
                    for_button_mine(x,y+1)
                if btns[x][x-1,y+1]['нажата?']==False:
                    for_button_mine(x-1,y+1)
                if btns[x][x-1,y]['нажата?']==False:
                    for_button_mine(x-1,y)

for i in range(5):
    bombs[cells[i][0]][cells[i][1]] = True
for i in bombs:
    print(i)

for i in range(10):
    step = {}
    for j in range(10):
        step[i, j] = {}
        step[i, j]['num'] = 0
        step[i, j]['кнопка'] = Button(root, width=2, height=1,command=lambda x=i,y=j:for_button_mine(x,y))
        step[i, j]['бомба'] = bombs[i][j]
        step[i, j]['координаты'] = [i, j]
        if i==0 or i==9 or j==0 or j==9:
            step[i,j]['видимость']=False
        else:
            step[i, j]['видимость'] = True
        mins=0
        
    btns.append(step)
for i in range(10):
    for j in range(10):
        if btns[i][i,j]['видимость']==True:
            btn=btns[i][i,j]['кнопка']
            btn.grid(row=i,column=j)

root.mainloop()