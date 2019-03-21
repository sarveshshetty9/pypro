#!python3
import time
import socket
import requests
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from DBHandler import *
from PIL import ImageTk, Image


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

        #---------------- FOR IMAGE ---------------- 
        
        from bs4 import BeautifulSoup
        
        res = requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
        #print(res)
        
        soup = BeautifulSoup(res.text, 'lxml')
        
        quote = soup.find('img',{"class":"p-qotd"})
        #print(quote)
        
        #print(quote['alt'])
        
        img_url = "https://www.brainyquote.com" + quote['data-img-url']
        #print(img_url)
        imagefile = "qotd.jpg"
        r = requests.get(img_url)
        with open(imagefile, 'wb') as f:
            f.write(r.content)
        '''
        root = Tk()
        img = ImageTk.PhotoImage(Image.open("qotd.jpg"))
        panel = Label(root, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        root.mainloop()'''
        
        # create the canvas, size in pixels
        canvas = Canvas(width = 300, height = 200, bg = 'yellow')
        # pack the canvas into a frame/form
        canvas.pack(expand = YES, fill = BOTH)
        # load the .gif image file
        # put in your own gif file here, may need to add full path
        # like 'C:/WINDOWS/Help/Tours/WindowsMediaPlayer/Img/mplogo.gif'
        gif1 = PhotoImage(file = 'qotd.jpg')
        # put gif image on canvas
        # pic's upper left corner (NW) on the canvas is at x=50 y=10
        canvas.create_image(50, 10, image = gif1, anchor = NW)
        # run it ...
        mainloop()
        
        import io
        import base64
        try:
            # Python2
            import Tkinter as tk
            from urllib2 import urlopen
        except ImportError:
    # Python3
    import tkinter as tk
    from urllib.request import urlopen
    root = tk.Tk()
    root.title("display a website image")
    # a little more than width and height of image
    w = 520
    h = 320
    x = 80
    y = 100
    # use width x height + x_offset + y_offset (no spaces!)
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    # this GIF picture previously downloaded to tinypic.com
    image_url = "http://i46.tinypic.com/r9oh0j.gif"
    image_byt = urlopen(image_url).read()
    image_b64 = base64.encodestring(image_byt)
    photo = tk.PhotoImage(data=image_b64)
    # create a white canvas
    cv = tk.Canvas(bg='white')
    cv.pack(side='top', fill='both', expand='yes')
    # put the image on the canvas with
    # create_image(xpos, ypos, image, anchor)
    cv.create_image(10, 10, image=photo, anchor='nw')
    root.mainloop()

        #---------------- FOR CITY NAME ---------------- 
        
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
            if (not rno.isdigit() or int(rno) < 1):
                messagebox.showerror("Wrong", "Rollnumber should be positive digits only.")
                entAddRno.delete(0, END)
                entAddRno.focus()
                return
            name = entAddName.get()
            if len(name) < 1:
                messagebox.showerror("Incomplete","Name is empty")
                entAddName.focus()
                return
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