#!python3
import time
import socket
import requests
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from DBHandler import *


class Splash(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.title("Welcome")
        self.geometry("300x300+450+300")

        try:
            socket.create_connection(("www.google.com", 80))
            res = requests.get("https://ipinfo.io/")
            print(res)
            data = res.json()
            print(data)
            city = data['city']
            print(city)

        except OSError:
            print("Check Network")

        lblcity = Label(self, text = city, font = ('arial', 10, 'bold'), width = 20)
        lblcity.pack(pady = 10)


        ## required to make window show before the program gets to the mainloop
        self.update()

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.withdraw()
        splash = Splash(self)

        ## setup stuff goes here
        self.title("Main Window")
    
        self.title("Student Management System")
        self.geometry("300x300+450+300")
        
        #---------------- datascience ---------------- 
        import socket

        try:
            socket.create_connection(("www.google.com", 80))
            print("You are connected.")

        except OSError as e:
            print(e)
            print("You are not connected")

        #---------------- root ---------------- 


        def open(x):
            self.withdraw()
            x.deiconify()

        def view():
            self.withdraw()
            viewFrame.deiconify()
            st.delete('1.0', END)
            data = viewStudent()
            st.insert(INSERT, data)

        def back(x):
            x.withdraw()
            self.deiconify()

        btnAdd = Button(self, text = "Add", bd = 5, font= ('arial', 10, 'bold'), width = 10, command = lambda: open(addFrame))
        btnView = Button(self, text = "View", bd = 5, font = ('arial', 10, 'bold'), width = 10, command = view)
        btnUpdate = Button(self, text = "Update", bd = 5, font= ('arial', 10, 'bold'), width = 10, command = lambda: open(updateFrame))
        btnDelete = Button(self, text = "Delete", bd = 5, font = ('arial', 10, 'bold'), width = 10, command = lambda: open(deleteFrame))

        btnAdd.pack(pady = 10)
        btnView.pack(pady = 10)
        btnUpdate.pack(pady = 10)
        btnDelete.pack(pady = 10)

        #---------------- addFrame ---------------- 

        addFrame = Toplevel(self)
        addFrame.title("Add Student")
        addFrame.geometry("300x300+450+300")
        addFrame.withdraw()

        def add():
            rno = entAddRno.get()
            if len(rno) == 0:
                messagebox.showerror("Incomplete","RollNumber is empty")
                entAddRno.focus()
                return
            if not rno.isdigit() or int(rno) < 1:
                messagebox.showerror("Wrong", "Rollnumber should be positive digits only.")
                entAddRno.delete(0, END)
                entAddRno.focus()
                return
            name = entAddName.get()
            if len(name) < 1:
                messagebox.showerror("Incomplete","Name is empty")
                entAddName.focus()
            addStudent(int(rno),name)
            entAddRno.delete(0, END)
            entAddName.delete(0, END)
            entAddRno.focus()

        lblAddRno = Label(addFrame, text = "Roll No.", font = ('arial', 10, 'bold'), width = 20)
        entAddRno = Entry(addFrame, bd = 5,  font = ('arial', 10, 'bold'), width = 20)
        lblAddName = Label(addFrame, text = "Name", font = ('arial', 10, 'bold'), width = 20)
        entAddName = Entry(addFrame, bd = 5,  font = ('arial', 10, 'bold'), width = 20)
        btnAdd = Button(addFrame, text = "Add" , bd = 5, font = ('arial', 10, 'bold'), width = 20, command = add)
        btnAddBack = Button(addFrame, text = "Back", bd = 5, font = ('arial', 10, 'bold'), width = 20, command = lambda: back(addFrame))
        lblAddRno.pack(pady = 10)
        entAddRno.pack(pady = 10)
        lblAddName.pack(pady = 10)
        entAddName.pack(pady = 10)
        btnAdd.pack(pady = 10)
        btnAddBack.pack(pady = 10)

        #---------------- viewFrame ---------------- 

        viewFrame = Toplevel(self)
        viewFrame.title("View Student")
        viewFrame.geometry("300x300+450+300")

        viewFrame.withdraw()
        st = scrolledtext.ScrolledText(viewFrame, width = 20, height = 10)
        btnViewBack = Button(viewFrame, text = "Back", bd = 5, font = ('arial', 10, 'bold'), width = 20, command = lambda: back(viewFrame))

        st.pack(pady = 10)
        btnViewBack.pack(pady = 10)

        #---------------- updateFrame ---------------- 

        updateFrame = Toplevel(self)
        updateFrame.title("Update Student")
        updateFrame.geometry("300x300+450+300")
        updateFrame.withdraw()

        def update():
            rno = entUpdateRno.get()
            if len(rno) == 0:
                messagebox.showerror("Incomplete ", "Rollnumber is empty.")
                entUpdateRno.focus()
                return
            if not rno.isdigit() or int(rno) < 1:
                messagebox.showerror("Wrong", "Rollnumber should be positive digits only.")
                entUpdateRno.delete(0, END)
                entUpdateRno.focus()
                return
            name = entUpdateName.get()
            if len(name) < 1:
                messagebox.showerror("Incomplete", "Name is Empty")
                entUpdateName.focus
                return
            updateStudent(int(rno),name)
            entUpdateRno.delete(0, END)
            entUpdateName.delete(0, END)
            entUpdateRno.focus()

        lblUpdateRno = Label(updateFrame, text = "Roll No.", font = ('arial', 10, 'bold'), width = 20)
        entUpdateRno = Entry(updateFrame, bd = 5,  font = ('arial', 10, 'bold'), width = 20)
        lblUpdateName = Label(updateFrame, text = "Name", font = ('arial', 10, 'bold'), width = 20)
        entUpdateName = Entry(updateFrame, bd = 5,  font = ('arial', 10, 'bold'), width = 20)
        btnUpdate = Button(updateFrame, text = "Update" , bd = 5, font = ('arial', 10, 'bold'), width = 20, command = update)
        btnUpdateBack = Button(updateFrame, text = "Back", bd = 5, font = ('arial', 10, 'bold'), width = 20, command = lambda: back(updateFrame))

        lblUpdateRno.pack(pady = 10)
        entUpdateRno.pack(pady = 10)
        lblUpdateName.pack(pady = 10)
        entUpdateName.pack(pady = 10)
        btnUpdate.pack(pady = 10)
        btnUpdateBack.pack(pady = 10)

        #----------------  deleteFrame ---------------- 

        deleteFrame = Toplevel(self)
        deleteFrame.title("Delete Student")
        deleteFrame.geometry("300x300+450+300")
        deleteFrame.withdraw()

        def delete():
            rno = entDeleteRno.get()
            if len(rno) == 0:
                messagebox.showerror("Incomplete ", "Rollnumber is empty.")
                entDeleteRno.focus()
                return
            if not rno.isdigit() or int(rno) < 1:
                messagebox.showerror("Wrong", "Rollnumber should be positive digits only.")
                entDeleteRno.delete(0, END)
                entDeleteRno.focus()
                return
            deleteStudent(int(rno))
            entDeleteRno.delete(0, END)
            entDeleteRno.focus()

        lblDeleteRno = Label(deleteFrame, text = "Roll No.", font = ('arial', 10, 'bold'), width = 20)
        entDeleteRno = Entry(deleteFrame, bd = 5,  font = ('arial', 10, 'bold'), width = 20)
        btnDelete = Button(deleteFrame, text = "Delete" , bd = 5, font = ('arial', 10, 'bold'), width = 20, command = delete)
        btnDeleteBack = Button(deleteFrame, text = "Back", bd = 5, font = ('arial', 10, 'bold'), width = 20, command = lambda: back(deleteFrame))

        lblDeleteRno.pack(pady = 10)
        entDeleteRno.pack(pady = 10)
        btnDelete.pack(pady = 10)
        btnDeleteBack.pack(pady = 10)

        ## simulate a delay while loading
        time.sleep(2)

        ## finished loading so destroy splash
        splash.destroy()

        ## show window again
        self.deiconify()

if __name__ == "__main__":
    app = App()
    app.mainloop()