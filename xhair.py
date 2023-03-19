from re import X
import tkinter as tk
from tkinter import CENTER

from PIL import Image, ImageTk, ImageOps

from pynput.keyboard import Key, Listener
import time


class XHair():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.img = None
        self.x = None

    def setimg(self, imgpath: str, x: str):
        file = Image.open(imgpath)
        file.convert("RGBA")
        self.x = x
        self.img = file.resize((x, x))


    def movementerror(self, imgpath: str):
        file = Image.open(imgpath)
        file.convert("RGBA")
        img = file.resize((self.x, self.x))
        self.mvmebg = ImageTk.PhotoImage(img)

        self.mvme = tk.Label(self.root, image=self.mvmebg, borderwidth=0)
        self.mvme.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.mvme.master.attributes('-transparentcolor', 'black', '-topmost', 1)

        self.mvme.pack()


    def run(self, mvmepath=None):
        print(self.img, self.x)
        if self.img == None or self.x == None:
            raise ValueError("Image not set")
        
        self.bg = ImageTk.PhotoImage(self.img)

        self.background_label = tk.Label(self.root, image=self.bg, borderwidth=0)
        self.background_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        screen_width = self.root.winfo_screenwidth()  # Width of the screen
        screen_height = self.root.winfo_screenheight() # Height of the screen
        
        # Calculate Starting X and Y coordinates for Window
        x = (screen_width/2) - (self.x/2)
        y = (screen_height/2) - (self.x/2)
        
        self.root.geometry('%dx%d+%d+%d' % (self.x, self.x, x, y))


        self.background_label.master.attributes('-transparentcolor', 'black', '-topmost', 1)


        self.background_label.pack()

        if mvmepath != None:
            self.movementerror(imgpath=mvmepath)
            listener = Listener(on_press=self._on_press, on_release=self._on_release)
            listener.start()

        self.root.mainloop()

    def _on_press(self, key):
        if '{0}'.format(key).replace("'", "") in ["w", "s", "a", "d"]:
            self.mvme.pack()
            self.background_label.pack_forget()


    def _on_release(self, key):
        if '{0}'.format(key).replace("'", "") in ["w", "s", "a", "d"]:
            time.sleep(0.2)
            self.background_label.pack()
            self.mvme.pack_forget()

        



