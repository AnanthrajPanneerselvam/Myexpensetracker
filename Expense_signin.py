from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import ImageTk,Image
import os
os.getcwd()

root=Tk()
root.geometry('950x500+300+200')
root.configure(bg="#fff")
root.title("Sign-In window")
root.iconbitmap("C:\python23\Tkinder project\key.ico")
root.resizable(0, 0)


#Creating Frames
topFrame=Frame(root, bg='grey')
topFrame.place(x=250)
headingFrame=Frame(root,width=350,height=350,bg="#fff")
headingFrame.place(x=490,y=50)
mainFrame=Frame(root, bg='white')
mainFrame.place(x=480,y=120)
user=StringVar()
passw=StringVar()
confpassw=StringVar()
mail_id=StringVar()

#Creating function to make Sign-in & Login

def signin():
    if (user.get()=='') or (passw.get()=='') or (confpassw.get()=='') or (mail_id.get()==''):
        messagebox.showerror('Error','All Fields are Required')
    elif passw.get()!=confpassw.get():
        messagebox.showerror('Error','Passwords Mismatch, Try Again')
    else:
        try:
            connection = pymysql.connect(host='localhost', user='root', password='Admin@123')
            conn=connection.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue, TRY AGAIN')
            return
    try:
        query='create database admin'
        conn.execute(query)
        query1='use admin'
        conn.execute(query1)
        query2='create table user(username varchar(100), password varchar(50), repassword varchar(50), mailid varchar(100))'
        conn.execute(query2)
    except:
        conn.execute('use admin')

    query3='select * from user where username = %s'
    conn.execute(query3,(user.get()))

    row=conn.fetchone()

    if row!=None:
        messagebox.showerror('Error','Username already exists')

    else:
        query='insert into user(username,password,repassword,mailid)values(%s,%s,%s,%s)'
        conn.execute(query,(user.get(),passw.get(),confpassw.get(),mail_id.get()))
        connection.commit()
        connection.close()
        messagebox.showinfo('Success','Account Created Successfully')
        

def clearFunc():
    user.set('user_name')
    passw.set('password')
    confpassw.set('confirm password')
    mail_id.set('example123@gmail.com')

def go_to_login():
    root.destroy()
    import Expense_login
    
#===================Add Image=================================
bg_image = Image.open("C:\python23\Tkinder project\sign_in.jpg")
bg_image = bg_image.resize((400,400))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(root,image=bg_photo)
bg_label.place(x=10, y=50)

#Creating Title Frame

title_label=Label(topFrame, text='Welcome to Expense Tracker',fg='#57a1f8',bg='white', padx=20, pady=5, font=('Tahoma',18))
title_label.pack()

#Creating Labels
heading=Label(headingFrame,text='Sign in',fg='#57a1f8',bg='white',font=('microsoft yahei UI light',23,'bold'))
heading.place(x=110,y=5)
username=Label(mainFrame,text="Username:",font=('Verdana',15), bg='white')
username.grid(row=2, column=0)
password=Label(mainFrame,text="Password:",font=('Verdana',15), bg='white')
password.grid(row=3, column=0)
confpassword=Label(mainFrame,text="Confirm Password:",font=('Verdana',15), bg='white')
confpassword.grid(row=4, column=0)
mailid=Label(mainFrame,text="Mail_ID:",font=('Verdana',15), bg='white')
mailid.grid(row=5, column=0)


#Creating Entry grids

#For Username
def enter(e):
    username_entry.delete(0,'end')

def leave(e):
    name=username_entry.get()
    if name=='':
        username_entry.insert(0,'user_name')
        
username_entry=Entry(mainFrame, textvariable=user, font=('Verdana',15))
username_entry.grid(row=2, column=1, padx=10, pady=10)
username_entry.insert(0,'user_name')
username_entry.bind("<FocusIn>",enter)
username_entry.bind("<FocusOut>",leave)

#For Password
def enter(e):
    password_entry.delete(0,'end')

def leave(e):
    name=password_entry.get()
    if name=='':
        password_entry.insert(0,'password')

password_entry=Entry(mainFrame, textvariable=passw, font=('Verdana',15), show='*')
password_entry.grid(row=3,column=1, padx=10, pady=10)
password_entry.insert(0,'password')
password_entry.bind("<FocusIn>",enter)
password_entry.bind("<FocusOut>",leave)

#For Confirm Password
def enter(e):
    repassword_entry.delete(0,'end')

def leave(e):
    name=repassword_entry.get()
    if name=='':
        repassword_entry.insert(0,'confirm password')

repassword_entry=Entry(mainFrame, textvariable=confpassw, font=('Verdana',15), show='*')
repassword_entry.grid(row=4,column=1, padx=10, pady=10)
repassword_entry.insert(0,'confirm password')
repassword_entry.bind("<FocusIn>",enter)
repassword_entry.bind("<FocusOut>",leave)

#For Mail-ID
def enter(e):
    mailid_entry.delete(0,'end')

def leave(e):
    name=mailid_entry.get()
    if name=='':
        mailid_entry.insert(0,'example123@gmail.com')

mailid_entry=Entry(mainFrame, textvariable=mail_id, font=('Verdana',15))
mailid_entry.grid(row=5,column=1, padx=10, pady=10)
mailid_entry.insert(0,'example123@gmail.com')
mailid_entry.bind("<FocusIn>",enter)
mailid_entry.bind("<FocusOut>",leave)

#Creating Sign-in and reset button

signin_button=Button(mainFrame,text='Sign in', fg='white', bg='#57a1f8', font=('Calibri',15),command=signin)
signin_button.grid(row=6, column=0)
reset_button=Button(mainFrame,text='Reset', fg='white', bg='#57a1f8', font=('Calibri',15),command=clearFunc)
reset_button.grid(row=6, column=1)


#Creating Login-in button
signin_button=Button(mainFrame,text='Already Signed in, Go to log in page>>',border=0,bg='white',font=('Times New Roman',15),command=go_to_login)
signin_button.grid(row=7,columnspan=2)



root.mainloop()


















































