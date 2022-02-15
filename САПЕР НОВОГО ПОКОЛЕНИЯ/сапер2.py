import random
from tkinter import *

root = Tk()
res=10
btns = []
cells = [[i, j] for i in range(1, res+1) for j in range(1, res+1)]
random.shuffle(cells)

bombs=[[False for _ in range(res+2)] for _ in range(res+2)]
def for_button_mine(x,y):
    global btns
    global res
    if btns[x][x,y]['видимость']==True:
        
        btns[x][x,y]['нажата?']=True
        btns[x][x,y]['кнопка'].config(state='disabled',background="#ddd")
        mins=0
        if btns[x][x,y]['бомба']==True:
            for i in range(res+2):
                for j in range(res+2):
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
                if btns[x-1][x-1,y-1]['нажата?']==False:
                    for_button_mine(x-1,y-1)
                if btns[x][x,y-1]['нажата?']==False:
                    for_button_mine(x,y-1)
                if btns[x+1][x+1,y-1]['нажата?']==False:
                    for_button_mine(x+1,y-1)
                if btns[x+1][x+1,y]['нажата?']==False:
                    for_button_mine(x+1,y)
                if btns[x+1][x+1,y+1]['нажата?']==False:
                    for_button_mine(x+1,y+1)
                if btns[x][x,y+1]['нажата?']==False:
                    for_button_mine(x,y+1)
                if btns[x-1][x-1,y+1]['нажата?']==False:
                    for_button_mine(x-1,y+1)
                if btns[x-1][x-1,y]['нажата?']==False:
                    for_button_mine(x-1,y)

for i in range(10):
    bombs[cells[i][0]][cells[i][1]] = True
for i in bombs:
    print(i)

for i in range(res+2):
    step = {}
    for j in range(res+2):
        step[i, j] = {}
        step[i, j]['num'] = 0
        step[i, j]['кнопка'] = Button(root, width=2, height=1,command=lambda x=i,y=j:for_button_mine(x,y))
        step[i, j]['бомба'] = bombs[i][j]
        step[i, j]['координаты'] = [i, j]
        step[i, j]['нажата?'] = False
        if i==0 or i==res+1 or j==0 or j==res+1:
            step[i,j]['видимость']=False
        else:
            step[i, j]['видимость'] = True
        mins=0
        
    btns.append(step)
for i in range(res+2):
    for j in range(res+2):
        if btns[i][i,j]['видимость']==True:
            btn=btns[i][i,j]['кнопка']
            btn.grid(row=i,column=j)

root.mainloop()