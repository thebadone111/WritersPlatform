#import modules
from tkinter import *
from tkinter import ttk
import mysql.connector
import reader as r

# Master window
class Start_window(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Welcome!")
        self.grid(column=0, row=0)
        self.main_window()

    def main_window(self):
        # Widgets / elements
        content = ttk.Frame(self.master)

        login_button = ttk.Button(content, text="Login", command=self.login_window_start)
        register_button = ttk.Button(content, text="Register", command=self.register_window_start)
        quit_button = ttk.Button(content, text="Quit", command=self.master.destroy)

        # Layout
        content.grid(column=0, row=0, sticky=(N,S,E,W))

        login_button.grid(column=1, row=1, pady=5, padx=5, sticky=(N,S,E,W))
        register_button.grid(column=2, row=1, pady=5, padx=5, sticky=(N,S,E,W))
        quit_button.grid(column=1, row=2, columnspan=2, pady=5, padx=5, sticky=(N,S,E,W))

        # Resizing 
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        content.columnconfigure(0, weight=2)
        content.columnconfigure(1, weight=1)
        content.columnconfigure(2, weight=1)
        content.columnconfigure(3, weight=2)
        content.rowconfigure(0, weight=2)
        content.rowconfigure(1, weight=1)
        content.rowconfigure(2, weight=1)
        content.rowconfigure(3, weight=2)

    def login_window_start(self):
        new_login = login_window(self.master)
        new_login.grab_set()
    
    def register_window_start(self):
        new_register = register_window(self.master)
        new_register.grab_set()


# Register window
class register_window(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Register window")
        self.grid()
        self.window()


    def window(self):
        # Widgets / elements
        title_label = ttk.Label(self, text="Register here!")

        username_label = ttk.Label(self, text="Username: ")
        self.username_string = StringVar()
        username_field = ttk.Entry(self, textvariable=self.username_string)

        password_label = ttk.Label(self, text="Password: ")
        self.password_string = StringVar()
        password_field = ttk.Entry(self, textvariable=self.password_string)

        quit_button = ttk.Button(self, text="Quit", command=self.destroy)
        register = ttk.Button(self, text="Register", command=self.register)

        # Layout 
        title_label.grid(column=2, row=0, pady=5, padx=5)
        username_label.grid(column=1, row=1, pady=5, padx=5)
        username_field.grid(column=2, row=1, columnspan=3, pady=5, padx=5, sticky=(E,W))
        password_label.grid(column=1, row=2, pady=5, padx=5)
        password_field.grid(column=2, row=2, columnspan=3, pady=5, padx=5, sticky=(E,W))
        register.grid(column=2, row=3, pady=5, padx=5, sticky=(S,E,W))
        quit_button.grid(column=2, row=4, pady=5, padx=5, sticky=(S,E,W))

        # Resizing
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
   

        
    def register(self):
        # Register logic + Mysql
        if len(self.username_string.get()) == 0:
            print("Please write username")
        elif len(self.password_string.get()) == 0:
            print("Please write password")
        else:
            mydb = mysql.connector.connect(
            host="localhost",
            user="Admin",
            password="BobHund123",
            database="test"
            )
            cursor = mydb.cursor()
            query = "SELECT * FROM customers WHERE username= %(username)s;"
            cursor.execute(query, {'username': str(self.username_string.get())})
            result = cursor.fetchall()
            if len(result) != 0:
                print("Username already used")
            else:
                query = "INSERT INTO customers (username, password) VALUES (%s, %s)"
                data = (str(self.username_string.get()), str(self.password_string.get()))
                cursor.execute(query, data)
                mydb.commit()
                print("Record inserted")
                self.destroy()

# Login window
class login_window(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Login window")
        self.grid()
        self.window()

    def window(self):
        # Widgets / elements
        title_label = ttk.Label(self, text="Login here!")

        username_label = ttk.Label(self, text="Username: ")
        self.username_string = StringVar()
        username_field = ttk.Entry(self, textvariable=self.username_string)
        

        password_label = ttk.Label(self, text="Password: ")
        self.password_string = StringVar()
        password_field = ttk.Entry(self, textvariable=self.password_string)
        
        login = ttk.Button(self, text="Login", command=self.login)
        quit_button = ttk.Button(self, text="Quit", command=self.destroy)

        # Layout
        title_label.grid(column=2, row=0, pady=5, padx=5)
        username_label.grid(column=1, row=1, pady=5, padx=5)
        username_field.grid(column=2, row=1, columnspan=3, pady=5, padx=5, sticky=(E,W))
        password_label.grid(column=1, row=2, pady=5, padx=5)
        password_field.grid(column=2, row=2, columnspan=3, pady=5, padx=5, sticky=(E,W))
        login.grid(column=2, row=3, pady=5, padx=5, sticky=(S,E,W))
        quit_button.grid(column=2, row=4, pady=5, padx=5, sticky=(S,E,W))


        # Resizing
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        
    def login(self):
        # Login logic + Mysql
        mydb = mysql.connector.connect(
        host="localhost",
        user="Admin",
        password="BobHund123",
        database="test"
        )
        cursor = mydb.cursor()
        query = "SELECT * FROM customers WHERE username= %(username)s;"
        cursor.execute(query, {'username': str(self.username_string.get())})
        result = cursor.fetchall()

        if len(result) != 0:
            print("username found")
            try:
                if result[0][2] == str(self.password_string.get()):
                    print("Login successful")
                    ## CLOSE EVERYTHING AND OPEN MAIN WINDOW
                    self.master.destroy()
                    r.start_main_window()
                else:
                    print("Login failed")
            except:
                print("if statement broke")
        else:
            print("username not found")

root = Tk()
start = Start_window(master=root)
start.mainloop()
