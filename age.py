from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import math
def male():
    global y
    y =70.8 
def female():
    global y 
    y =75.6
def x ():
    x = entry1.get()


    year = 2021-int(x)
    day = int(x)*365
    min = int(day)*1440
    sec = int(min)*60
    new_window = Tk()
    new_window.geometry("500x300")
    label = Label(new_window,text="You lived "+str(year)+" year"+"\n"+"You lived "+str(day)+" day."+"\n"+"You lived "+str(min)+" minute"+"\n"+"You lived "+
    str(sec)+" second.",font=("Arial",15)
    )
    label.place(x=30,y=100)
    bar = Progressbar(new_window,orient=HORIZONTAL,length=300)
    bar.pack()
    
    percent = (int(year)/int(y))*100
    percent = round(percent)
    bar['value']+=percent
    label_percent = Label(new_window,font=("Arial",15),text="You lived %"+str(percent)+" percent of your life")
    label_percent.pack()
    new_window.mainloop()
    


window = Tk()
label1 = Label(window,font=("Arial",30),text="Enter your year of birth")
label1.pack()
entry1 = Entry(window,font=("Arial",30)) 
entry1.pack()
button = Button(window,command=x,text="Submit")
button.pack()
button_male = Button(window,text="male",command=male)
button_male.pack()
button_female = Button(window,text="female",command=female)
button_female.pack()
window.mainloop()
