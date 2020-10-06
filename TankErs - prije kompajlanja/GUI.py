import pygame
import tkinter as tk
from tkinter import *
import os

class App:
    def __init__(self, master):

        #PHOTO
        self.photo = tk.PhotoImage(file="graphics/8-bit-tank.png")
        Label(root, image=self.photo, bg=None).pack(side=tk.TOP)

        self.frame = Frame(master)
        self.frame.pack()

        #TOP BAR
        title = root.title("TankErs")
        root.iconbitmap(default="cog.ico")

        #BUTTONS
        play = Button(self.frame,
                   text = 'PLAY',
                   command = self.openFile)
        play.pack(side=tk.TOP, pady=10)

        options = tk.Button(self.frame,
                            text="SHOW FPS",
                            command="")
        options.pack(side=tk.TOP, pady=10)

        quit = tk.Button(self.frame,
                         text="QUIT",
                         fg="red",
                         command=root.destroy)
        quit.pack(side=tk.BOTTOM, pady=10)

    def openFile(self):
        os.startfile("Main.exe")
        root.destroy()

root = tk.Tk()
app = App(root)
root.mainloop()


