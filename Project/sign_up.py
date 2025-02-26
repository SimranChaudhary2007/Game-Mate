from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
import tkinter.font as font
import runpy
import sqlite3

win=Tk()
win.configure(bg="#0C0A0B")
win.attributes("-fullscreen",True)

screen_width = win.winfo_screenwidth()
screen_height=win.winfo_screenheight()

a=Frame(win,width=screen_width, height=35,bg="white")
a.pack(side=TOP, fill=X)
title=Label(a, text="Game Mate",font=("Semi Bold Italic",15,"bold"), bg="white").place(x=36,y=3)
img=Image.open("Project_images/icon.jpg")
img=img.resize((20,20))
new_logo=ImageTk.PhotoImage(img)
image=Label(image=new_logo,border=2,bg="#989898").place(x=5,y=5)

def min():
    win.iconify()

def on_enter(i):
    btn2['background'] = "red"

def on_leave(i):
    btn2['background'] = "white"

def max():
    msg_box = messagebox.askquestion('Exit Application', 'Are you sure you want to close the application?', icon='warning')
    if msg_box == 'yes':
        win.destroy()

label1 = LabelFrame(win, height=30, bg="white").place(x=0, y=0)
buttonFont = font.Font(size=14)

btn2 = Button(a, text="✕", command=max, width=4, bg="white", border=0, font=buttonFont)
btn2.place(x=screen_width-50, y=0)
btn2.bind('<Enter>', on_enter)
btn2.bind('<Leave>', on_leave)

def enter(i):
    btn['background'] = "#989898"

def leave(i):
    btn['background'] = "white"

btn = Button(a, text="-", command=min, width=4, bg="white", border=0, font=buttonFont)
btn.place(x=screen_width - 100, y=0)  
btn.bind('<Enter>', enter)
btn.bind('<Leave>', leave)

img = Image.open("Project_images/Background.jpg")
img = img.resize((screen_width, screen_height))
img = ImageTk.PhotoImage(img)
image_label = Label(win, image=img)
image_label.place(x=-2, y=35)

b=Frame(win,width=500,height=550,bg="#0C0A0B",highlightthickness=1)
b.place(x=screen_width-800,y=screen_height/4)

heading=Label(b,text="Sign up",fg="white",font=("Microsoft YaHei UI Light",23,"bold"),bg="#0C0A0B")
heading.place(x=180,y=1)

def on1_enter(e):
    name=first_name.get()
    if name=="First Name":
        first_name.delete(0,"end")

def on1_leave(e):
    name=first_name.get()
    if name=="":
        first_name.insert(0,'First Name')

first_name=Entry(b,fg="white",border=0,font=("Microsoft YaHei UI Light",12),bg="#0C0A0B",insertbackground="white")
first_name.place(x=10,y=95)
first_name.insert(0,"First Name")
first_name.bind("<FocusIn>", on1_enter)
first_name.bind("<FocusOut>", on1_leave)


Frame(b,width=450,height=2,bg="white").place(x=5,y=120)

def on2_enter(e):
    name=last_name.get()
    if name=="Last Name":
        last_name.delete(0,"end")

def on2_leave(e):
    name=last_name.get()
    if name=="":
        last_name.insert(0,'Last Name')

last_name=Entry(b,fg="white",border=0,font=("Microsoft YaHei UI Light",12),bg="#0C0A0B",insertbackground="white")
last_name.place(x=10,y=165)
last_name.insert(0,"Last Name")
last_name.bind("<FocusIn>", on2_enter)
last_name.bind("<FocusOut>", on2_leave)


Frame(b,width=450,height=2,bg="white").place(x=5,y=190)

def on3_enter(e):
    name=mail.get()
    if name=="E-mail":
        mail.delete(0,"end")

def on3_leave(e):
    name=mail.get()
    if name=="":
        mail.insert(0,'E-mail')

mail=Entry(b,fg="white",border=0,font=("Microsoft YaHei UI Light",12),bg="#0C0A0B",insertbackground="white")
mail.place(x=10,y=235)
mail.insert(0,"E-mail")
mail.bind("<FocusIn>", on3_enter)
mail.bind("<FocusOut>", on3_leave)


Frame(b,width=450,height=2,bg="white").place(x=5,y=260)


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

code1=Entry(b,fg="white",border=0,font=("Microsoft YaHei UI Light",12),bg="#0C0A0B",insertbackground="white")
code1.place(x=10,y=305)
code1.insert(0,"Create password")
code1.bind('<FocusIn>', on4_enter)
code1.bind('<FocusOut>', on4_leave)

Frame(b,width=450,height=2,bg="white").place(x=5,y=330)

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
eyebutton1.place(x=435,y=305)

def on5_enter(e):
    name=code2.get()
    if name=="Confirm password":
        code2.delete(0,"end")
        code2.config(show="*")

def on5_leave(e):
    name=code2.get()
    if name=="":
        code2.config(show="")
        code2.insert(0,'Confirm password')

code2=Entry(b,fg="white",border=0,font=("Microsoft YaHei UI Light",12),bg="#0C0A0B",insertbackground="white")
code2.place(x=10,y=375)
code2.insert(0,"Confirm password")
code2.bind('<FocusIn>', on5_enter)
code2.bind('<FocusOut>', on5_leave)

Frame(b,width=450,height=2,bg="white").place(x=5,y=400)

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
eyebutton2.place(x=435,y=375)

buttonFont1=font.Font(size=12)

label=Label(b,text="Already have an account?",fg="white",bg="#0C0A0B",font=("Microsoft YaHei UI Light",12))
label.place(x=95,y=485)

def enter1(event):
    login["background"]="#989898"

def leave1(event):
    login["background"]="#0C0A0B"

def login_page():
    win.destroy()
    runpy.run_path("Project/log_in.py")

login=Button(b,width=7,text="Log in",font=buttonFont1,border=0,bg="#0C0A0B",cursor="hand2",fg="white",activebackground="white",command=login_page)
login.place(x=290,y=485)
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
    email=mail.get()
    password1=code1.get()
    password2=code2.get()
    global img
    if  Firstname=="First  Name" or Lastname=="Last  Name" or email=="E-mail" or password1=="Create password" or password2=="Confirm password" :
        messagebox.showinfo("Error","All fields are required!")
    elif "@" not in email or email.endswith(".com")==False:
        messagebox.showerror("Error","Enter a valid Email")
    elif password1!=password2:
        messagebox.showerror("Error","Passwords do not match. Please try again.")
    else:
        messagebox.showinfo("Success","Sign-up successful! Please log in to continue.")
        data1=sqlite3.connect("sign_up.db")
        d1=data1.cursor()

        d1.execute("""CREATE TABLE IF NOT EXISTS signup(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  first_name TEXT NOT NULL,
                  last_name TEXT NOT NULL,  
                  emails TEXT NOT NULL,
                  password1 TEXT NOT NULL,
                  password2 TEXT NOT NULL
        )""")

        try:
            d1.execute("""
                    INSERT INTO signup (first_name,last_name,emails,password1,password2)
                    VALUES (?,?,?,?,?)
                    """, (Firstname, Lastname, email, password1, password2))
            data1.commit()
            data1.close()
        except Exception as e:
           print("Error",e)

        win.destroy()
        runpy.run_path(r"Project/log_in.py")
            
signup=Button(b,width=50,height=2,text="Sign up",bg="white",fg="black",border=0,activebackground="#989898",font=buttonFont2,command=sign_up)
signup.place(x=10,y=435)
signup.bind('<Enter>',enter2)
signup.bind('<Leave>',leave2)

win.mainloop()