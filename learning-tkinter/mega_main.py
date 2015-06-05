try:
    from tkinter import Tk, Label, Canvas, PhotoImage
except ImportError:
    raise ImportError('This game only works with Python3')

from os import path

IMAGES_PATH = path.join(path.dirname(__file__), 'images')

root = Tk()

MEGAMAN = PhotoImage(file=path.join(IMAGES_PATH, "megaman.gif"))
DIDDY = PhotoImage(file=path.join(IMAGES_PATH, "diddy.gif"))
BACKGROUND = PhotoImage(file=path.join(IMAGES_PATH, "background.gif"))


def criar_fase():
    root.title('MegaKongPython')
    root.geometry("400x300")
    root.resizable(0, 0)

    diddy = Label(image=DIDDY)
    megaman = Label(image=MEGAMAN)
    fundo = Label(image=BACKGROUND)

    diddy.pack()
    megaman.pack()
    fundo.pack() 

    root.mainloop()


if __name__ == '__main__':
    criar_fase()
