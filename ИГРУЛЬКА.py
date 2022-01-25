from tkinter import *
root = Tk()
btns=[]
for i in range(10):
    step={}
    for j in range(10):
        step[i,j] = {}
        step[i,j]['кнопка']=Button(root,width=2,height=1)
        step[i,j]['num'] = 0
    btns.append(step)
for i in range(10):
    for j in range(10):
        btn=btns[i][i,j]['кнопка']
        btn.grid(row=i,column=j)
    
root.mainloop()