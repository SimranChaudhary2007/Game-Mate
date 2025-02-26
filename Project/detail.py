from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
import tkinter.font as font
import runpy
import sqlite3

win=Tk()
win.configure(bg="#0C0A0B")
win.attributes("-fullscreen",True)

a=Frame(win,width=2000,height=35,bg="white").place(x=0,y=0)
title=Label(a, text="Game Mate",font=("Semi Bold Italic",15,"bold"), bg="white").place(x=36,y=3)
img=Image.open("Project_images/icon.jpg")
img=img.resize((20,20))
new_logo=ImageTk.PhotoImage(img)
image=Label(image=new_logo,border=2,bg="#989898").place(x=5,y=5)
screen_width =win.winfo_screenwidth()
screen_height=win.winfo_screenheight()

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
btn2.pack(anchor="ne")
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

def back():
    win.destroy()
    runpy.run_path("Project/specs_checker.py")
    
def enter1(i):
    btn3['background']="#989898"
def leave1(i):
    btn3['background']="white"

btn3=Button(win,text="<<",width=4,bg="white",border=0,font=buttonFont,command=back)
btn3.place(x=screen_width-150,y=0)
btn3.bind('<Enter>', enter1)
btn3.bind('<Leave>', leave1)

logo_img=Image.open("Project_images/logo.jpeg")
logo_img=logo_img.resize((150,150))
logo=ImageTk.PhotoImage(logo_img)
image=Label(image=logo,border=0).place(x=5,y=80)

heading=Label(text="GAME MATE",font=("Gabriola",100),bg="#0C0A0B",fg="white").place(x=170,y=35)

title_detail=Frame(win,width=2000,height=40,bg="#B1B1B1").place(x=0,y=240)
Label(title_detail,text="Details",font=("Bahnschrift",19,"bold"),bg="#B1B1B1").place(x=950,y=243)


data1=sqlite3.connect("sign_up.db")
d1=data1.cursor()

detailframe = Frame(win,width=600,height=(screen_height/2)+100,bg="#0C0A0B",highlightthickness=2,highlightbackground="white")
detailframe.place(x=700,y=320)             

F=Label(detailframe,text="First Name",font=("Microsoft YaHei UI Light",15),fg="white",bg="#0C0A0B").place(x=42,y=25)
first_name=Entry(detailframe,width=25,fg="black",bg="#F1F1F1",border=2,font=14)
first_name.place(x=42,y=60)

L=Label(detailframe,text="Last Name",font=("Microsoft YaHei UI Light",15),fg="white",bg="#0C0A0B").place(x=42,y=125)
last_name=Entry(detailframe,width=25,fg="black",bg="#F1F1F1",border=2,font=14)
last_name.place(x=42,y=160)

E=Label(detailframe,text="Email",font=("Microsoft YaHei UI Light",15),fg="white",bg="#0C0A0B").place(x=42,y=208)
mail=Entry(detailframe,width=25,fg="black",bg="#F1F1F1",border=2,font=14)
mail.place(x=42,y=243)

p=Label(detailframe,text="Password",font=("Microsoft YaHei UI Light",15),fg="white",bg="#0C0A0B").place(x=42,y=291)
code1=Entry(detailframe,width=25,fg="black",bg="#F1F1F1",border=2,font=14,show="*")
code1.place(x=42,y=326)

def hide1():
    eyeclose1.config(file="Project_images/hide.png")
    code1.config(show="*")
    eyebutton1.config(command=show1)

def show1():
    eyeclose1.config(file="Project_images/view.png")
    code1.config(show="")
    eyebutton1.config(command=hide1)

eyeclose1=PhotoImage(file="Project_images/hide.png")
eyebutton1=Button(detailframe,image=eyeclose1,bg="#F1F1F1",border=0,command=show1,activebackground="#F1F1F1",cursor="hand2")
eyebutton1.place(x=300,y=332)

with open("logged_user.txt", "r") as f:
    logged_in_email = f.read()

d1.execute("SELECT * FROM signup WHERE emails=?", (logged_in_email,))
user_info = d1.fetchone()

if user_info:  
    first_name.delete(0, "end")
    first_name.insert(0, user_info[1])  
    
    last_name.delete(0, "end")
    last_name.insert(0, user_info[2])  
    
    mail.delete(0, "end")
    mail.insert(0, user_info[3])  
    
    code1.delete(0, "end")
    code1.insert(0, user_info[4]) 

data1.commit()

def update_profile():
    new_first_name = first_name.get()
    new_last_name = last_name.get()
    new_email = mail.get()
    current_password = code1.get()

    if not new_first_name or not new_last_name or not new_email or not current_password:
        messagebox.showerror("Error", "All fields are required!")
        return

    data1 = sqlite3.connect("sign_up.db")
    d1 = data1.cursor()

    with open("logged_user.txt", "r") as f:
        logged_in_email = f.read()

    d1.execute("SELECT * FROM signup WHERE emails = ?", (logged_in_email,))
    user = d1.fetchone()

    if not user or user[4] != current_password:
        messagebox.showerror("Error", "Current password is incorrect.")
        data1.close()
        return

    d1.execute("""
        UPDATE signup 
        SET first_name = ?, last_name = ?, emails = ?
        WHERE emails = ?
    """, (new_first_name, new_last_name, new_email, logged_in_email))

    data1.commit()
    
    if new_email != logged_in_email:
        with open("logged_user.txt", "w") as f:
            f.write(new_email)
    
    data1.close()
    messagebox.showinfo("Success", "Profile updated successfully!")

def delete_account():
    msg_box = messagebox.askquestion("Delete Account", "Are you sure you want to delete your account? This action cannot be undone.", icon='warning')
    if msg_box == 'yes':
        data1 = sqlite3.connect("sign_up.db")
        d1 = data1.cursor()

        with open("logged_user.txt", "r") as f:
            logged_in_email = f.read()

        d1.execute("DELETE FROM signup WHERE emails = ?", (logged_in_email,))
        data1.commit()
        data1.close()
        
        messagebox.showinfo("Account Deleted", "Your account has been successfully deleted.")
        win.destroy()
        runpy.run_path("Project/log_in.py")
            
def update_password(current_code, new_code):
    current_password = current_code.get()
    new_password = new_code.get()

    if not current_password or not new_password:
        messagebox.showerror("Error", "Both fields are required!")
        return

    data1 = sqlite3.connect("sign_up.db")
    d1 = data1.cursor()

    with open("logged_user.txt", "r") as f:
        logged_in_email = f.read()

    d1.execute("SELECT * FROM signup WHERE emails = ? AND password1 = ?", (logged_in_email, current_password))
    user = d1.fetchone()

    if user:
        d1.execute("""
            UPDATE signup 
            SET password1 = ?, password2 = ?
            WHERE emails = ? AND password1 = ?
        """, (new_password, new_password, logged_in_email, current_password))

        data1.commit()
        data1.close()
        messagebox.showinfo("Success", "Password updated successfully! Login with new password to continue.")
        win.destroy()
        runpy.run_path("Project/log_in.py")
    else:
        messagebox.showerror("Error", "Current password is incorrect.")
        data1.close()

def edit():
    global root, eyeclose2, eyeclose3, eyebutton2, eyebutton3
    root=Toplevel()
    root.configure(bg="#0C0A0B")
    root.geometry('350x300')
    root.resizable(0,0)
    root.iconbitmap('Project_images/icon1.ico')
    root.title("Game Mate - Change Password")

    current_label=Label(root,text="Current password",fg="white",bg="#0C0A0B",font=("Microsoft YaHei UI Light",10))
    current_label.place(x=5,y=20)
    current_code=Entry(root,font=10,border=2,background="#F1F1F1",show="*")
    current_code.place(x=5,y=50)

    def hide2():
        eyeclose2.config(file="Project_images/hide.png")
        current_code.config(show="*")
        eyebutton2.config(command=show2)

    def show2():
        eyeclose2.config(file="Project_images/view.png")
        current_code.config(show="")
        eyebutton2.config(command=hide2)

    eyeclose2=PhotoImage(file="Project_images/hide.png")
    eyebutton2=Button(root,image=eyeclose2,bg="#F1F1F1",border=0,command=show2,activebackground="#F1F1F1",cursor="hand2")
    eyebutton2.place(x=205,y=55)

    new_password=Label(root,text="New password",fg="white",bg="#0C0A0B",font=("Microsoft YaHei UI Light",10))
    new_password.place(x=5,y=90)
    new_code=Entry(root,border=2,font=10,background="#F1F1F1",show="*")
    new_code.place(x=5,y=120)

    def hide3():
        eyeclose3.config(file="Project_images/hide.png")
        new_code.config(show="*")
        eyebutton3.config(command=show3)

    def show3():
        eyeclose3.config(file="Project_images/view.png")
        new_code.config(show="")
        eyebutton3.config(command=hide3)

    eyeclose3=PhotoImage(file="Project_images/hide.png")
    eyebutton3=Button(root,image=eyeclose3,bg="#F1F1F1",border=0,command=show3,activebackground="#F1F1F1",cursor="hand2")
    eyebutton3.place(x=205,y=125)

    buttonFont=font.Font(size=10)
    Save=Button(root,text="Save",bg="#71FC9B",font=buttonFont,border=3,command=lambda: update_password(current_code, new_code))
    Save.place(x=150,y=200)


buttonFont=font.Font(size=14)

Update= Button(detailframe, text="Update Profile", font=buttonFont, bg="#71FC9B", border=3, command=update_profile)
Update.place(x=42, y=420)

Change= Button(detailframe, text="Change Password", font=buttonFont, bg="#71FC9B", border=3, command=edit)
Change.place(x=220, y=420)

Delete= Button(detailframe, text="Delete Account", font=buttonFont, bg="#FF6B6B", border=3, command=delete_account)
Delete.place(x=430, y=420)

def logout():
    msg_box=messagebox.askquestion("Confirm Logout","Are you sure you want to logout?")
    if msg_box == 'yes':
        win.destroy()
        runpy.run_path("Project/log_in.py")

logout_button = Button(text="Logout", font=buttonFont, bg="#0C0A0B", fg="white", border=0,command=logout)
logout_button.place(x=1800, y=80)


win.mainloop()