from tkinter import *
from time import strftime

myWindows = Tk()
myWindows. title('My Clock')

def time():
    myTime = strftime('%H:%M:%S %p')
    clock.config(text = myTime)
    clock.after(1000, time)

clock = Label(myWindows, font = ('arial', 40, 'bold'),
                                background = 'dark orange',
                                foreground = 'white')
clock.pack(anchor = 'center')
time()

mainloop()