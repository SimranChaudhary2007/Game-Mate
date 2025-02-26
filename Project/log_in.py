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

b=Frame(win,width=500,height=350,bg="#0C0A0B",highlightthickness=1)
b.place(x=screen_width-800,y=screen_height/3)

heading=Label(b,text="Log in",fg="white",font=("Microsoft YaHei UI Light",23,"bold"),bg="#0C0A0B")
heading.place(x=180,y=1)

def on1_enter(e):
    name=mail.get()
    if name=="E-mail":
        mail.delete(0,"end")

def on1_leave(e):
    name=mail.get()
    if name=="":
        mail.insert(0,'E-mail')

mail=Entry(b,fg="white",border=0,font=("Microsoft YaHei UI Light",12),bg="#0C0A0B",insertbackground="white")
mail.place(x=10,y=95)
mail.insert(0,"E-mail")
mail.bind("<FocusIn>", on1_enter)
mail.bind("<FocusOut>", on1_leave)


Frame(b,width=450,height=2,bg="white").place(x=5,y=120)

def on2_enter(e):
    name=code.get()
    if name=="Password":
        code.delete(0,"end")
        code.config(show="*")

def on2_leave(e):
    name=code.get()
    if name=="":
        code.config(show="")
        code.insert(0,"Password")

code=Entry(b,fg="white",border=0,font=("Microsoft YaHei UI Light",12),bg="#0C0A0B",insertbackground="white")
code.place(x=10,y=165)
code.insert(0,"Password")
code.bind('<FocusIn>', on2_enter)
code.bind('<FocusOut>', on2_leave)

Frame(b,width=450,height=2,bg="white").place(x=5,y=190)

def hide():
    eyeclose.config(file="Project_images/eyeclose.png")
    code.config(show="*")
    eyebutton.config(command=show)

def show():
    eyeclose.config(file="Project_images/eyeopen.png")
    code.config(show="")
    eyebutton.config(command=hide)

eyeclose=PhotoImage(file="Project_images/eyeclose.png")
eyebutton=Button(b,image=eyeclose,bg="#0C0A0B",border=0,command=show,activebackground="#0C0A0B",cursor="hand2")
eyebutton.place(x=435,y=165)

def specs_checker_page():
    email_value = mail.get()
    password_value = code.get()
    data2 = sqlite3.connect("sign_up.db")
    d2 = data2.cursor()

    d2.execute("SELECT * FROM signup WHERE emails=? AND password1=?", (email_value, password_value))
    user = d2.fetchone()
    if user:
        with open("logged_user.txt", "w") as f:
            f.write(email_value)
        
        data2.commit()
        data2.close()
        win.destroy()
        runpy.run_path("Project/specs_checker.py")
    else:
        messagebox.showerror("Error", "Invalid information")


buttonFont1=font.Font(size=12)

def enter1(event):
    login["background"]="#989898"

def leave1(event):
    login["background"]="white"

login=Button(b,width=50,height=2,text="Log in",bg="white",fg="black",border=0,activebackground="#989898",font=buttonFont1,command=specs_checker_page)
login.place(x=10,y=230)
login.bind('<Enter>',enter1)
login.bind('<Leave>',leave1)

label=Label(b,text="Don't have an account?",fg="white",bg="#0C0A0B",font=("Microsoft YaHei UI Light",12))
label.place(x=110,y=290)

def enter2(event):
    signup["background"]="#989898"

def leave2(event):
    signup["background"]="#0C0A0B"

def signup_page():
    win.destroy()
    runpy.run_path('Project/sign_up.py') 

signup=Button(b,width=7,text="Sign up",font=buttonFont1,border=0,bg="#0C0A0B",cursor="hand2",fg="white",activebackground="white",command=signup_page)
signup.place(x=285,y=290)
signup.bind('<Enter>',enter2)
signup.bind('<Leave>',leave2)

buttonFont2=font.Font(size=13)

win.mainloop()