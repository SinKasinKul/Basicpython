from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
width = 500
hight = 300
GUI.title('Calculate Test on GUI.')
GUI.geometry('500x800')

bg = PhotoImage(file='cat.png')
BG = Label(GUI,image=bg)
BG.pack()

vLableMain = Label(GUI,text="Please input cat total.",font=(None,20))
vLableMain.pack()

v_quantity = StringVar() # valiable text
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None,20))
E1.pack()

def CalCat():
    try:
        quan = float(v_quantity.get())
        vCal = quan * 250
        messagebox.showinfo('Total amount',f'Total Cat is : {vCal}')
        v_quantity.set('')
    except:
        messagebox.showwarning('Warning','Please input Only numeric.')
        v_quantity.set('')

B1 = ttk.Button(GUI,text='Calculate', command=CalCat)
B1.pack(ipadx=20,ipady=15)
B1.pack()

GUI.mainloop() # Alway running app