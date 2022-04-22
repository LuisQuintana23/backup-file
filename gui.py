import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

class Interface():
    def __init__(self, win):
        self.win = win
        self.win.geometry("300x300")
        self.win.title("Secure File")
        self.win.resizable(0,0)

        self.frame1 = tk.Frame(self.win)


        #Labels
        self.lb_title = tk.Label(
            self.frame1,
            text="Select a file with follow",
            font=("Calibri", 13)
            )

        self.lb_file = tk.Label(
            self.frame1,
            text="No file Selected",
            font=("Calibri", 13)
            )

        ##BUTTONS
        self.btn_follow = tk.Button(
            self.frame1, 
            text="Follow",
            font=("Calibri", 11),
            command=self.select_file
            )

        self.btn_exit = tk.Button(
            self.frame1, 
            text="Exit",
            font=("Calibri", 11),
            bg="red",
            fg="white",
            command=self.out
            #Add same function than unfollow
            )

         
        elements = [self.lb_title, self.lb_file, self.frame1, self.btn_follow, self.btn_exit]

        self.packet(elements)




    def packet(self, elements):
        for lmnt in elements:
            lmnt.pack(expand=True)

    def select_file(self):
        filetypes = (
            ('Text File', '*.txt'),
            ('Phothoshop file', '*.psd'),
            # add more extensions
            ('All files', '*.*')
        )

        file_name = fd.askopenfilename(
            title='Select File',
            initialdir='./',
            filetypes=filetypes)

        showinfo(
            title = 'Selected File',
            message = f"Path: {file_name}"
        )

        self.lb_file.config(text=file_name)


    def run(self):
        self.win.mainloop()

    def out(self):
        exit()    
