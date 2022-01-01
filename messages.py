#import modules
from tkinter import *
from tkinter import ttk
import mysql.connector

# Master window
class Messages_Window(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Messages and Followings")
        self.main()

    def main(self):
        # Widgets / elements
        content = ttk.Frame(self)

        title_label = ttk.Label(content, text="Shitty")

        # Layout
        content.grid(column=0, row=0, sticky=(N,S,E,W))

        title_label.grid(column=1, row=0, pady=5, padx=5, sticky=(N))

        # Resizing 
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        
        content.columnconfigure(0, weight=0)
        content.rowconfigure(0, weight=0)