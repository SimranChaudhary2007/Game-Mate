from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from  tkinter import ttk
import tkinter.font as font
import runpy
import sqlite3
import psutil
import platform
import subprocess
import cpuinfo

win = Tk()
win.configure(bg="#0C0A0B")
win.attributes("-fullscreen", True)

a = Frame(win, width=2000, height=35, bg="white").place(x=0, y=0)
title = Label(a, text="Game Mate", font=("Semi Bold Italic", 15, "bold"), bg="white").place(x=36, y=3)
img = Image.open("Project_images/icon.jpg")
img = img.resize((20, 20))
new_logo = ImageTk.PhotoImage(img)
image = Label(image=new_logo, border=2, bg="#989898").place(x=5, y=5)
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

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

btn = Button(a, text="-", command=min, width=4, bg="white", border=0, font=buttonFont)
btn.place(x=screen_width - 100, y=0)

def enter(i):
    btn['background'] = "#989898"

def leave(i):
    btn['background'] = "white"

btn.bind('<Enter>', enter)
btn.bind('<Leave>', leave)

title_frame = Frame(win, width=1800, height=55, bg="#0C0A0B").place(x=0, y=70)
heading1 = Label(title_frame, text="Analyse your system and find the best games for your PC.", font=("Medium", 30, "bold", "underline"), fg="white", bg="#0C0A0B").place(x=80, y=70)
img = Image.open("Project_images/computer.png")
img = img.resize((50, 50))
logo = ImageTk.PhotoImage(img)
image = Label(image=logo, border=2, bg="#0C0A0B").place(x=10, y=70)

buttonFont = font.Font(size=15)

details_button = Button(text="Details", font=buttonFont, bg="#0C0A0B", fg="white", border=0)
details_button.place(x=1720, y=80)

logout_button = Button(text="Logout", font=buttonFont, bg="#0C0A0B", fg="white", border=0)
logout_button.place(x=1800, y=80)



# main body left side
body_frame = Frame(win, width=1000, height=850, bg="white").place(x=470, y=170)
heading2 = Label(body_frame, text="Tell us about your PC.", font=("Medium", 28, "bold"), fg="black", bg="white").place(x=500, y=190)

canvas1 = Canvas(body_frame, width=450, height=2, bg="#207CD1", highlightthickness=0)
canvas1.create_line(0, 1, 450, 1, fill="#207CD1")
canvas1.place(x=500, y=250)

canvas2 = Canvas(body_frame, width=2, height=850, bg="black", highlightthickness=0)
canvas2.create_line(1, 0, 1, 850, fill="black")
canvas2.place(x=1050, y=170)

# string var to hold specification
platform_var = StringVar()
processor_var = StringVar()
graphicscard_var = StringVar()
memory_var = StringVar()

def get_gpu_name():
    try:
        # Try to get GPU name using system commands
        if platform.system() == "Windows":
            result = subprocess.run(['wmic', 'path', 'win32_VideoController', 'get', 'name'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            lines = result.stdout.split('\n')
            gpu_names = [line.strip() for line in lines if line.strip() and line.strip() != "Name"]
            if gpu_names:
                return ', '.join(gpu_names)
        elif platform.system() == "Linux":
            result = subprocess.run(['lspci'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            for line in result.stdout.split('\n'):
                if 'VGA compatible controller' in line or '3D controller' in line:
                    return line.split(': ')[-1]
        elif platform.system() == "Darwin":
            result = subprocess.run(['system_profiler', 'SPDisplaysDataType'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            for line in result.stdout.split('\n'):
                if 'Chipset Model' in line:
                    return line.split(': ')[-1].strip()
    except Exception as e:
        print("Error:", e)  
        
    return "N/A"

def get_system_specs():
    gpu_name = get_gpu_name()
    cpu_info = cpuinfo.get_cpu_info()
    processor_name = cpu_info.get('brand_raw', platform.processor())

    specs = {
        "platform": platform.system(),
        "processor": processor_name,
        "cpu_count": psutil.cpu_count(logical=True),
        "gpu": gpu_name,
        "memory": f"{round(psutil.virtual_memory().total / (1024**3))} GB"
    }
    return specs



specs_detected = False
def display_specs():
    global specs_detected
    specs = get_system_specs()
    platform_var.set(f"{specs['platform']}")
    processor_var.set(specs['processor'])
    graphicscard_var.set(specs['gpu'])
    memory_var.set(specs['memory'])
    specs_detected = True
    
pl_img = Image.open("Project_images/platform.png")
pl_img = pl_img.resize((20, 20))
pl_logo = ImageTk.PhotoImage(pl_img)
pl_label = Label(body_frame, image=pl_logo, bg="white")
pl_label.place(x=500, y=290)

platform_label = Label(body_frame, text="Platform", font=("Extra Light", 22), fg="black", bg="white")
platform_label.place(x=525, y=280)


platform_options=["Windows","Linux/SteamOS","macOS"]
entry1 = ttk.Combobox(body_frame, width=30, font=("Extra Light", 18),values=platform_options, textvariable=platform_var)
entry1.place(x=500, y=330, height=50)

pr_img = Image.open("Project_images/processor.png")
pr_img = pr_img.resize((20, 20))
pr_logo = ImageTk.PhotoImage(pr_img)
pr_label = Label(body_frame, image=pr_logo, bg="white")
pr_label.place(x=500, y=410)

processor_label = Label(body_frame, text="Processor", font=("Extra Light", 22), fg="black", bg="white")
processor_label.place(x=525, y=400)

processor_options=["Intel Core i9-13900K","Intel Core i7-12700K","Intel Core i5-13600K","Intel Core i3-12100F",
                   "AMD Ryzen 9 7950X","AMD Ryzen 7 7800X3D","AMD Ryzen 5 7600X","Intel Core i5-11400F",
                   "AMD Ryzen 7 5800X","AMD Ryzen 5 5600G"]
entry2 = ttk.Combobox(body_frame, width=30, font=("Extra Light", 18), values=processor_options , textvariable=processor_var)
entry2.place(x=500, y=450, height=50)

gc_img = Image.open("Project_images/graphic_card.png")
gc_img = gc_img.resize((20, 20))
gc_logo = ImageTk.PhotoImage(gc_img)
gc_label = Label(body_frame, image=gc_logo, bg="white")
gc_label.place(x=500, y=530)

graphicscard_label = Label(body_frame, text="Graphics-Card", font=("Extra Light", 22), fg="black", bg="white")
graphicscard_label.place(x=525, y=520)

graphicscard_options=["NVIDIA RTX 4090","NVIDIA RTX 4080","NVIDIA RTX 4070 Ti","NVIDIA RTX 4060","AMD Radeon RX 7900 XTX",
                      "AMD Radeon RX 7800 XT","AMD Radeon RX 6700 XT","Intel Arc A770","NVIDIA GTX 1660 Super","NVIDIA RTX 3060 T"]
entry3 = ttk.Combobox(body_frame, width=30, font=("Extra Light", 18), values=graphicscard_options, textvariable=graphicscard_var)
entry3.place(x=500, y=570, height=50)


m_img = Image.open("Project_images/memory.png")
m_img = m_img.resize((20, 20))
m_logo = ImageTk.PhotoImage(m_img)
m_label = Label(body_frame, image=m_logo, bg="white")
m_label.place(x=500, y=650)

memory = Label(body_frame, text="Memory", font=("Extra Light", 22), fg="black", bg="white")
memory.place(x=525, y=640)

memory_options=["1 GB","2 GB"," 4 GB","6 GB","8 GB","12 GB","16 GB","24 GB","32 GB","64 Gb(or more)"]
entry4 = ttk.Combobox(body_frame, width=30, font=("Extra Light", 18), values=memory_options, textvariable=memory_var)
entry4.place(x=500, y=690, height=50)

d_img = Image.open("Project_images/detect.png")
d_img = d_img.resize((15, 15))
d_logo = ImageTk.PhotoImage(d_img)

buttonFont1 = font.Font(size=16)

detect = Button(body_frame, text="Detect specs", image=d_logo, compound=LEFT, font=buttonFont1, bg="#24D3FA", command=display_specs)
detect.place(x=650, y=810)

detect.image = d_logo

r_img = Image.open("Project_images/icon1.png")
r_img = r_img.resize((15, 15))
r_logo = ImageTk.PhotoImage(r_img)

def recommendation_page():
    platform_val = platform_var.get().strip()
    processor_val = processor_var.get().strip()
    graphicscard_val = graphicscard_var.get().strip()
    memory_val = memory_var.get().strip()

    if not (platform_val and processor_val and graphicscard_val and memory_val):
        messagebox.showinfo("Error", "All fields are required.")
        return

    if not specs_detected:
        if platform_val not in platform_options:
            messagebox.showerror("Error", "Please select the options given in the list or let the system detect it.")
            return
        if processor_val not in processor_options:
            messagebox.showerror("Error", "Please select the options given in the list or let the system detect it.")
            return
        if memory_val not in memory_options:
            messagebox.showerror("Error", "Please select the options given in the list or let the system detect it.")
            return

    win.destroy()
    runpy.run_path("Project/game_recom.py")



recom = Button(body_frame, text="What games my PC can run?", image=r_logo, compound=LEFT, font=buttonFont1, bg="#71FC9B", command=recommendation_page)
recom.place(x=580, y=880)

recom.image = r_logo



# main body right side
info_text = """How it works?

🔹Tell your PC specs or let the system detect them.
🔹We analyse your system specifications.
🔹Find out what games your PC can run."""

text_label1 = Label(win, text=info_text, font=("Arial", 12), fg="black", bg="white", justify=LEFT)
text_label1.place(x=1070, y=200)

canvast1 = Canvas(body_frame, width=390, height=2, bg="black", highlightthickness=0)
canvast1.create_line(0, 0, 390, 1, fill="black")
canvast1.place(x=1065, y=320)

benefit_text = """Why use this tool?

🔹Avoid lag and crashes.
🔹Get the best setting for your pc.
🔹Find games optimized for your system."""


text_label2 = Label(win, text=benefit_text, font=("Arial", 12), fg="black", bg="white", justify=LEFT)
text_label2.place(x=1070, y=360)

canvast2= Canvas(body_frame, width=390, height=2, bg="black", highlightthickness=0)
canvast2.create_line(0, 0, 390, 1, fill="black")
canvast2.place(x=1065, y=480)

tips_text="""Want better gaming performance?

🔹 Close background apps
🔹 Use an SSD for faster load times
🔹 Keep your drivers updated"""

text_label3 = Label(win, text=tips_text, font=("Arial", 12), fg="black", bg="white", justify=LEFT)
text_label3.place(x=1070, y=520)

canvast3= Canvas(body_frame, width=390, height=2, bg="black", highlightthickness=0)
canvast3.create_line(0, 0, 390, 1, fill="black")
canvast3.place(x=1065, y=640)

funfact_text="""💡 Did you know?

Upgrading from an HDD to an SSD canboost
game loading speeds by up to 5x!"""

text_label4 = Label(win, text=funfact_text, font=("Arial", 12), fg="black", bg="white", justify=LEFT)
text_label4.place(x=1070, y=680)

canvast4= Canvas(body_frame, width=390, height=2, bg="black", highlightthickness=0)
canvast4.create_line(0, 0, 390, 1, fill="black")
canvast4.place(x=1065, y=800)

fotter_text="""Game Mate - Helping you find the best 
games for your PC.
Powered by RAWG API"""

text_label5 = Label(win, text=fotter_text, font=("Arial", 12,"bold"), fg="black", bg="white",justify=LEFT)
text_label5.place(x=1070, y=860)

win.mainloop()