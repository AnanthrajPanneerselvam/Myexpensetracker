from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import ImageTk,Image
import os
os.getcwd()

connection = pymysql.connect(host='localhost', user='root', password='Admin@123', database='admin')
conn= connection.cursor()

root=Tk()
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.title("Login window")
root.iconbitmap("C:\python23\Tkinder project\key.ico")
root.resizable(0, 0)


topFrame=Frame(root, bg='grey')
topFrame.place(x=250)
headingFrame=Frame(root,width=350,height=350,bg="#fff")
headingFrame.place(x=490,y=50)
mainFrame=Frame(root, bg='white')
mainFrame.place(x=480,y=120)
user=StringVar()
passw=StringVar()

#Creating function to make login & Sign-in

def login():
    username = username_entry.get()
    password = password_entry.get()
    vals = (username, password)
    select_query = "SELECT * FROM `user` WHERE `username` = %s and `password` = %s"
    conn.execute(select_query, vals)
    user = conn.fetchone()
    if user is not None:
        messagebox.showinfo('Info','Login Success')
        root.destroy()
        import Tracker
    else:
        messagebox.showwarning('Error','Wrong username or password')

def clearFunc():
    user.set("")
    passw.set("")

def go_to_signin():
    root.destroy()
    import Expense_signin
    
#===================Add Image=================================
bg_image = Image.open("C:\python23\Tkinder project\login.jpg")
bg_image = bg_image.resize((400,400))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(root,image=bg_photo)
bg_label.place(x=10, y=50)

#Creating Title Frame

title_label=Label(topFrame, text='Welcome to Expense Tracker',fg='#57a1f8',bg='white', padx=20, pady=5, font=('Tahoma',18))
title_label.pack()

#Creating Labels
heading=Label(headingFrame,text='Log in',fg='#57a1f8',bg='white',font=('microsoft yahei UI light',23,'bold'))
heading.place(x=110,y=5)
username=Label(mainFrame,text="Username:",font=('Verdana',16), bg='white')
username.grid(row=2, column=0)
password=Label(mainFrame,text="Password:",font=('Verdana',16), bg='white')
password.grid(row=3, column=0)

#Creating Entry grids
def enter(e):
    username_entry.delete(0,'end')

def leave(e):
    name=username_entry.get()
    if name=='':
        username_entry.insert(0,'user_name')
        
username_entry=Entry(mainFrame, textvariable=user, font=('Verdana',16))
username_entry.grid(row=2, column=1, padx=10, pady=20)
username_entry.insert(0,'user_name')
username_entry.bind("<FocusIn>",enter)
username_entry.bind("<FocusOut>",leave)

def enter(e):
    password_entry.delete(0,'end')

def leave(e):
    name=password_entry.get()
    if name=='':
        password_entry.insert(0,'password')

password_entry=Entry(mainFrame, textvariable=passw, font=('Verdana',16), show='*')
password_entry.grid(row=3,column=1, padx=10, pady=20)
password_entry.insert(0,'password')
password_entry.bind("<FocusIn>",enter)
password_entry.bind("<FocusOut>",leave)

#Creating Login and reset button

login_button=Button(mainFrame,text='Login', fg='white', bg='#57a1f8', font=('Calibri',16),command=login)
login_button.grid(row=4, column=0)
reset_button=Button(mainFrame,text='Reset', fg='white', bg='#57a1f8', font=('Calibri',16),command=clearFunc)
reset_button.grid(row=4, column=1)


#Creating Sign-in button
signin_button=Button(mainFrame,text='Don\'t have Logged in yet, Go to sign in>>',border=0,bg='white',font=('Times New Roman',16),command=go_to_signin)
signin_button.grid(row=5,columnspan=2)



root.mainloop()


















































