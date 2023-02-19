from re import X
import tkinter as tk
from tkinter import CENTER

from PIL import Image, ImageTk

class XHair():
    def __init__(self, r:int) -> None:
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.r = r

    def use(self, imgpath: str):
        file = Image.open(imgpath)


        resize = file.resize((self.r, self.r))

        bg = ImageTk.PhotoImage(resize)

        background_label = tk.Label(self.root, image=bg, borderwidth=0)
        background_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        screen_width = self.root.winfo_screenwidth()  # Width of the screen
        screen_height = self.root.winfo_screenheight() # Height of the screen
        
        # Calculate Starting X and Y coordinates for Window
        x = (screen_width/2) - (self.r/2)
        y = (screen_height/2) - (self.r/2)
        
        self.root.geometry('%dx%d+%d+%d' % (self.r, self.r, x, y))


        background_label.master.attributes('-transparentcolor', 'black', '-topmost', 1)


        background_label.pack()

        self.root.mainloop()

