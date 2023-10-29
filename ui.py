import tkinter as tk
import tkinter.ttk

from tkinter import *
from tkinter.ttk import *

import cv2
from PIL import Image, ImageTk
from tqdm import tqdm

from camera import Camera
from generator import Generator
width, height = 800, 600

gen = Generator()


class MainMenu:
    cam: Camera

    def __init__(self, cam:Camera):
        self.cam = cam

        self.root = tk.Tk()
        self.root.bind('<Escape>', lambda e: self.root.quit())

        self.progress = tkinter.ttk.Progressbar(self.root, orient="horizontal", length=200, mode="determinate")
        self.lmain = tk.Label(self.root)
        self.prompt_input = tk.Entry(self.root, width=100, borderwidth=5, font="Arial 20")
        self.prompt_input.place(height=10)
        self.prompt_negative_input = tk.Entry(self.root, width=100, borderwidth=5)
        self.text_button = tk.Button(self.root, text="Run", command=self.on_run)

        self.prompt_input.pack(pady=10, padx=10)
        self.prompt_negative_input.pack()
        self.text_button.pack()
        self.lmain.pack()
        self.progress.pack(pady=10, padx=10)
        
        self.show_frame()
        self.root.mainloop()

    def on_run(self):
        gen.generate(self.prompt_input.get())


    def show_frame(self):
        imgtk = self.cam.get_capture_for_tkinter()
        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)
        self.lmain.after(10, self.show_frame)
