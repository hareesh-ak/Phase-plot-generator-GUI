# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 22:01:31 2022

@author: Hareesh
"""


## LV-system solver
from PIL import ImageTk, Image
import tkinter
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as solv

r=.2
a=.1
b=.3
m=.2
Tf = 50
N=1000
time=np.linspace(0,Tf,N)

def f(t,X):
    x,y=X
    xdot=r*x - a*y*x
    ydot=b*y*x - m*y 
    return xdot,ydot

def print_IC(x0,y0):
    """ prints the input inital conditions in frame1"""
    
    
    solve_sys(float(x0), float(y0))
    IC_label = tkinter.Label(frame1, text = f'Initial X :{float(x0)}, Initial Y : {float(y0)} ',bg='cyan')
    plot_button = tkinter.Button(frame1,text='Plot',command =lambda : plot_image())
    IC_label.grid(row = 2, column=0,columnspan=4 )
    plot_button.grid(row=3,column=0,columnspan=4)
    x0_entry.delete(0,tkinter.END);y0_entry.delete(0,tkinter.END)
    x0_entry.insert(0,'1');y0_entry.insert(0,'1')
    

def plot_image():
    #global value
    for widgets in frame2.winfo_children():
        widgets.destroy()
    
    img = ImageTk.PhotoImage(Image.open('frame2_fig.png'))
    img_label = tkinter.Label(frame2,image=img)
    img_label.img = img
    img_label.pack()    

def solve_sys(x0,y0):
    z = solv.solve_ivp(f,t_span=[0,Tf],y0=np.array([x0,y0]),t_eval=time)
    X,Y = z.y[0],z.y[1]
    plt.ioff()
    plt.plot(X,Y)
    plt.savefig('frame2_fig.png')
    plt.close()

root = tkinter.Tk()
root.title('Phase plot generator')
root.geometry('800x800')
root.resizable(1,1)

frame1 = tkinter.LabelFrame(root,bg = 'cyan',text='Intial conditions for LV system',borderwidth = 10,width=800,height=200)
frame2 = tkinter.LabelFrame(root,text = 'Phase plots',width=800,height=600)

frame1.pack(fill='both',expand=True)
frame2.pack(fill='both',expand=True)
frame1.grid_propagate(False)
frame2.pack_propagate(False)

## labels and entry-fields for initial conditions x & y
x0_label = tkinter.Label(frame1, text='Initial X',bg='cyan')
x0_entry = tkinter.Entry(frame1, width=40, borderwidth=5)
x0_entry.insert(0,'1')
y0_label = tkinter.Label(frame1, text='Initial Y',bg='cyan')
y0_entry = tkinter.Entry(frame1, width=40, borderwidth=5)
y0_entry.insert(0,'1')
Enter_button = tkinter.Button(frame1, text ='Enter',bg='cyan',command = lambda: print_IC(x0_entry.get(),y0_entry.get()),borderwidth=5)




x0_entry.grid(row=0,column=0,padx=5,pady=5)
y0_entry.grid(row=0,column=1,padx=5,pady=5)
x0_label.grid(row=1,column=0,padx=5,pady=5)
y0_label.grid(row=1,column=1,padx=5,pady=5)
#y0_label.grid_propagate(0)
Enter_button.grid(row=0,column=2,padx=3,pady=5)



"""
x0 = int(x0_entry.get())
y0 = int(y0_entry.get())

z = solv.solve_ivp(f,t_span=[0,Tf],y0=np.array([x0,y0]))
X,Y = z.y[0],z.y[1]



plt.ioff()
plt.plot(X,Y)
plt.savefig(fname='frame2_fig.png')
plt.close()
"""
#Run mainloop
root.mainloop()