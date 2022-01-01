#import modules
from tkinter import *
from tkinter import ttk
import mysql.connector
import messages as m

# Master window
class Main_window(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Happy Reading!")
        self.main()
    
    def get_data(self):
        db = mysql.connector.connect(
            host="localhost",
            user="Admin",
            password="BobHund123",
            database="test"
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM customers")
        result = cursor.fetchall()

        text = []
        author = []

        for x in result:
            text.append(str(x[3]))
            author.append(str(x[1]))
        
        return text, author


    def main(self):
        # Widgets / elements
        self.content = ttk.Frame(self.master)

        self.title_label = ttk.Label(self.content, text="Shitty")

        # header buttons
        self.settings_button = ttk.Button(self.content, text="Settings", command=self.settings_window)
        self.messages_button = ttk.Button(self.content, text="Messages", command=self.messages_window)
        

        # footer buttons
        self.right_button = ttk.Button(self.content, text="Interested", command=self.right)
        self.left_button = ttk.Button(self.content, text="Not interested", command=self.left)
        

        # Main text window
        self.main_frame = ttk.Frame(self.content, borderwidth=5, relief="ridge")

        self.index = 0

        self.text_arr, self.author_arr = self.get_data()
        author = "Author: " + self.author_arr[self.index]

        self.author = ttk.Label(self.main_frame, text=author)
        self.main_text = Text(self.main_frame)
        
        
        self.main_text.insert('1.0', self.text_arr[self.index])

        
        # Layout
        self.content.grid(column=0, row=0, sticky=(N,S,E,W))

        self.title_label.grid(column=1, row=0, pady=5, padx=5, sticky=(N))
        self.settings_button.grid(column=2, row=0, pady=5, padx=5, sticky=(N,E)) 
        self.messages_button.grid(column=0, row=0, pady=5, padx=5, sticky=(N,W)) 

        self.main_frame.grid(column=0, row=1, padx=5, columnspan=3, rowspan=3, sticky=(N,S,E,W))
        self.author.grid(column=0, row=0, pady=5, padx=5, sticky=(N, W))
        self.main_text.grid(column=0, row=1, sticky=(N,S,E,W))
    
        self.right_button.grid(column=2, row=4, pady=5, padx=5, sticky=(S, W))
        self.left_button.grid(column=0, row=4, pady=5, padx=5, sticky=(S,E))

        # Relative weight - fixing resizing window problem 
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.content.columnconfigure(0, weight=0)
        self.content.columnconfigure(1, weight=3)
        self.content.columnconfigure(2, weight=0)

        self.content.rowconfigure(0, weight=0)
        self.content.rowconfigure(1, weight=5)
        self.content.rowconfigure(2, weight=5)
        self.content.rowconfigure(3, weight=5)
        self.content.rowconfigure(4, weight=3)

        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=0)
        self.main_frame.rowconfigure(1, weight=1)



    def right(self):
        # Right button
        self.index += 1

        author = "Author: " + self.author_arr[self.index]
        self.author = ttk.Label(self.main_frame, text=author)
        self.author.grid(column=0, row=0, pady=5, padx=5, sticky=(N, W))

        self.main_text.replace('1.0', 'end', self.text_arr[self.index])


    def left(self):
        # Left button
        self.index -= 1
        
        author = "Author: " + self.author_arr[self.index]
        self.author.destroy()
        self.author = ttk.Label(self.main_frame, text=author)
        self.author.grid(column=0, row=0, pady=5, padx=5, sticky=(N, W))

        self.main_text.replace('1.0', 'end', self.text_arr[self.index])

    def messages_window(self):
        # Messages / followed 
        self.start_messages_window = m.Messages_Window(self.master)
        self.start_messages_window.grab_set()
    
    def settings_window(self):
        # settings for shit i guess
        print("Nice job pressing a button idiot")
    


def start_main_window():
  root = Tk()
  main = Main_window(master=root) 
  main.mainloop()


# start_main_window()