import tkinter
from time import strftime

def tic():
    relogio['text'] = strftime('%H:%M:%S')

def tac():
    tic()
    relogio.after(1000, tac)

relogio = tkinter.Label()
relogio['text'] = '19:14:00'
relogio['font'] = 'Helvetica 120 bold'
relogio.pack()
tac()
relogio.mainloop()
