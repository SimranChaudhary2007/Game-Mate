from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
import tkinter.font as font
import runpy
import sqlite3

win=Tk()
win.configure(bg="white")
win.attributes("-fullscreen",True)

a=Frame(win,width=2000,height=35,bg="white").place(x=0,y=0)
title=Label(a, text="Game Mate",font=("Semi Bold Italic",15,"bold"), bg="white").place(x=36,y=3)
img=Image.open("Project_images/icon.jpg")
img=img.resize((20,20))
new_logo=ImageTk.PhotoImage(img)
image=Label(image=new_logo,border=2,bg="#989898").place(x=5,y=5)
screen_width = win.winfo_screenwidth()
screen_height=win.winfo_screenheight()

def min():
    win.iconify()
def on_enter(i):
    btn2['background']="red"
def on_leave(i):
    btn2['background']="white"
def max():
    msg_box =messagebox.askquestion('Exit Application', 'Are you sure you want to close the application?',icon='warning')
    if msg_box == 'yes':
        win.destroy()

label1=LabelFrame(win,height=30,bg="white").place(x=0,y=0)
buttonFont = font.Font(size=14)
btn2=Button(a,text="✕", command=max,width=4,bg="white",border=0,font=buttonFont)
btn2.pack(anchor="ne")
btn2.bind('<Enter>',on_enter)
btn2.bind('<Leave>',on_leave)

btn=Button(a,text="-", command=min,width=4,bg="white",border=0,font=buttonFont)
btn.place(x=screen_width-100,y=0)
def enter(i):
    btn['background']="#989898"
def leave(i):
    btn['background']="white"
btn.bind('<Enter>',enter)
btn.bind('<Leave>',leave)

img = Image.open("Project_images/Background.jpg")
img = img.resize((screen_width, screen_height))


img = ImageTk.PhotoImage(img)


image_label = Label(win, image=img)
image_label.place(x=-2, y=35)

b=Frame(win,width=500,height=600,bg="#0C0A0B").place(x=1200,y=270)

heading=Label(b,text="Sign up",fg="white",font=("Microsoft YaHei UI Light",23,"bold"),bg="#0C0A0B")
heading.place(x=1390,y=300)

def on1_enter(e):
    first_name.delete(0,"end")

def on1_leave(e):
    name=first_name.get()
    if name=="":
        first_name.insert(0,'First Name')

first_name=Entry(b,fg="white",border=0,font=("Microsoft YaHei UI Light",12),bg="#0C0A0B")
first_name.place(x=1218,y=395)
first_name.insert(0,"First Name")
first_name.bind("<FocusIn>", on1_enter)
first_name.bind("<FocusOut>", on1_leave)


Frame(b,width=450,height=2,bg="white").place(x=1215,y=420)

def on2_enter(e):
    last_name.delete(0,"end")

def on2_leave(e):
    name=last_name.get()
    if name=="":
        last_name.insert(0,'Last Name')

last_name=Entry(b,fg="white",border=0,font=("Microsoft YaHei UI Light",12),bg="#0C0A0B")
last_name.place(x=1218,y=465)
last_name.insert(0,"Last Name")
last_name.bind("<FocusIn>", on2_enter)
last_name.bind("<FocusOut>", on2_leave)


Frame(b,width=450,height=2,bg="white").place(x=1215,y=490)

def on3_enter(e):
    email.delete(0,"end")

def on3_leave(e):
    name=email.get()
    if name=="":
        email.insert(0,'E-mail')

email=Entry(b,fg="white",border=0,font=("Microsoft YaHei UI Light",12),bg="#0C0A0B")
email.place(x=1218,y=535)
email.insert(0,"E-mail")
email.bind("<FocusIn>", on3_enter)
email.bind("<FocusOut>", on3_leave)


Frame(b,width=450,height=2,bg="white").place(x=1215,y=560)


def on4_enter(e):
    name=code1.get()
    if name=="Create password":
        code1.delete(0,"end")
        code1.config(show="*")

def on4_leave(e):
    name=code1.get()
    if name=="":
        code1.config(show="")
        code1.insert(0,"Create password")

code1=Entry(b,fg="white",border=0,font=("Microsoft YaHei UI Light",12),bg="#0C0A0B")
code1.place(x=1218,y=605)
code1.insert(0,"Create password")
code1.bind('<FocusIn>', on4_enter)
code1.bind('<FocusOut>', on4_leave)

Frame(b,width=450,height=2,bg="white").place(x=1215,y=630)

def hide1():
    eyeclose1.config(file="Project_images/eyeclose.png")
    code1.config(show="*")
    eyebutton1.config(command=show1)

def show1():
    eyeclose1.config(file="Project_images/eyeopen.png")
    code1.config(show="")
    eyebutton1.config(command=hide1)

eyeclose1=PhotoImage(file="Project_images/eyeclose.png")
eyebutton1=Button(b,image=eyeclose1,bg="#0C0A0B",border=0,command=show1,activebackground="#0C0A0B",cursor="hand2")
eyebutton1.place(x=1645,y=605)

def on5_enter(e):
    name=code2.get()
    if name=="Confirm password":
        code2.delete(0,"end")
        code2.config(show="*")

def on5_leave(e):
    name=code2.get()
    if name=="":
        code2.congig(show="")
        code2.insert(0,'Confirm password')

code2=Entry(b,fg="white",border=0,font=("Microsoft YaHei UI Light",12),bg="#0C0A0B")
code2.place(x=1218,y=675)
code2.insert(0,"Confirm password")
code2.bind('<FocusIn>', on5_enter)
code2.bind('<FocusOut>', on5_leave)

Frame(b,width=450,height=2,bg="white").place(x=1215,y=700)

def hide2():
    eyeclose2.config(file="Project_images/eyeclose.png")
    code2.config(show="*")
    eyebutton2.config(command=show2)

def show2():
    eyeclose2.config(file="Project_images/eyeopen.png")
    code2.config(show="")
    eyebutton2.config(command=hide2)

eyeclose2=PhotoImage(file="Project_images/eyeclose.png")
eyebutton2=Button(b,image=eyeclose2,bg="#0C0A0B",border=0,command=show2,activebackground="#0C0A0B",cursor="hand2")
eyebutton2.place(x=1645,y=675)

buttonFont1=font.Font(size=12)

label=Label(b,text="Already have an account?",fg="white",bg="#0C0A0B",font=("Microsoft YaHei UI Light",12))
label.place(x=1305,y=785)

def enter1(event):
    login["background"]="#989898"

def leave1(event):
    login["background"]="#0C0A0B"

def login_page():
    win.destroy()
    runpy.run_path("Project/log_in.py")

login=Button(b,width=7,text="Log in",font=buttonFont1,border=0,bg="#0C0A0B",cursor="hand2",fg="white",activebackground="white",command=login_page)
login.place(x=1500,y=785)
login.bind('<Enter>',enter1)
login.bind('<Leave>',leave1)

buttonFont2=font.Font(size=13)

def enter2(event):
    signup["background"]="#989898"

def leave2(event):
    signup["background"]="white"

def sign_up():
    Firstname=first_name.get()
    Lastname=last_name.get()
    emails=email.get()
    password1=code1.get()
    password2=code2.get()
    global img
    if  Firstname=="First  Name" or Lastname=="Last  Name" or emails=="E-mail" or password1=="Create password" or password2=="Confirm password" :
        messagebox.showinfo("Error","All fields are required!")
    elif "@" not in emails or emails.endswith(".com")==False:
        messagebox.showerror("Error","Enter a valid Email")
    elif password1!=password2:
        messagebox.showerror("Error","Passwords do not match. Please try again.")
    else:
        messagebox.showinfo("Success","Sign-up successful! Please log in to continue.")
        data1=sqlite3.connect("signup.db")
        d1=data1.cursor()

        d1.execute("""CREATE TABLE IF NOT EXISTS sign(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  first_name TEXT NOT NULL,
                  last_name TEXT NOT NULL,  
                  emails TEXT NOT NULL,
                  password1 TEXT NOT NULL,
                  password2 TEXT NOT NULL
        )""")

        try:
            d1.execute("""
                    INSERT INTO sign (first_name,last_name,emails,password1,password2)
                    VALUES (?,?,?,?,?)
                    """, (Firstname, Lastname, emails, password1, password2))
            data1.commit()
            data1.close()
        except Exception as e:
            messagebox.showerror("Error",e)

        win.destroy()
        runpy.run_path(r"Project/log_in.py")
            
signup=Button(b,width=50,height=2,text="Sign up",bg="white",fg="black",border=0,activebackground="#989898",font=buttonFont2,command=sign_up)
signup.place(x=1215,y=735)
signup.bind('<Enter>',enter2)
signup.bind('<Leave>',leave2)

win.mainloop()