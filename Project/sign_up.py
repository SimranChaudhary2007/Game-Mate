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
img=Image.open(r"Project/icon.jpg")
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

img = Image.open(r"Project/Background.jpg")
img = img.resize((screen_width, screen_height))


img = ImageTk.PhotoImage(img)


image_label = Label(win, image=img)
image_label.place(x=-2, y=35)

b=Frame(win,width=500,height=600,bg="#0C0A0B").place(x=1200,y=270)

heading=Label(b,text="Sign up",fg="white",font=("Microsoft YaHei UI Light",23,"bold"),bg="#0C0A0B")
heading.place(x=1390,y=300)

def on1_enter(e):
    user.delete(0,"end")

def on1_leave(e):
    name=user.get()
    if name=="":
        user.insert(0,'E-mail')

user=Entry(b,fg="white",border=0,font=("Microsoft YaHei UI Light",12),bg="#0C0A0B")
user.place(x=1218,y=395)
user.insert(0,"E-mail")
user.bind("<FocusIn>", on1_enter)
user.bind("<FocusOut>", on1_leave)


Frame(b,width=450,height=2,bg="white").place(x=1215,y=420)


def on2_enter(e):
    code1.delete(0,"end")

def on2_leave(e):
    name=code1.get()
    if name=="":
        code1.insert(0,'Create password')

code1=Entry(b,fg="white",border=0,font=("Microsoft YaHei UI Light",12),bg="#0C0A0B")
code1.place(x=1218,y=465)
code1.insert(0,"Create password")
code1.bind('<FocusIn>', on2_enter)
code1.bind('<FocusOut>', on2_leave)

Frame(b,width=450,height=2,bg="white").place(x=1215,y=490)

def on3_enter(e):
    code2.delete(0,"end")

def on3_leave(e):
    name=code2.get()
    if name=="":
        code2.insert(0,'Confirm password')

code2=Entry(b,fg="white",border=0,font=("Microsoft YaHei UI Light",12),bg="#0C0A0B")
code2.place(x=1218,y=535)
code2.insert(0,"Confirm password")
code2.bind('<FocusIn>', on3_enter)
code2.bind('<FocusOut>', on3_leave)

Frame(b,width=450,height=2,bg="white").place(x=1215,y=560)

Button(b,width=60,height=2,text="Sign up",bg="white",fg="black",border=0,cursor="hand2").place(x=1230,y=610)

label=Label(b,text="Already have an account?",fg="white",bg="#0C0A0B",font=("Microsoft YaHei UI Light",10))
label.place(x=1330,y=660)

sign_up=Button(b,width=7,text="Log in",border=0,bg="#0C0A0B",cursor="hand2",fg="white")
sign_up.place(x=1490,y=660)


win.mainloop()

